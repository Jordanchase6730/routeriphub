/**
 * RouterIPHub - High Performance Client Engine
 * Zero dependencies, ultra-fast, robust event delegation for global search, dark/light theme switching, and diagnostics.
 */

// Global state
let siteSearchIndex = [];
let isSearchIndexLoaded = false;
let activeSearchFilter = 'all';
let currentResults = [];
let selectedResultIndex = -1;
let routersData = [];

// Initialize immediately if DOM is ready, or on DOMContentLoaded
function initApp() {
  initThemeToggle();
  initMobileNav();
  initGlobalSiteSearch();
  initSearch();
  initCopyButtons();
  initFaqAccordion();
  initInstantPrefetch();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initApp);
} else {
  initApp();
}

/* ==========================================================================
   1. Toast Notification Helper
   ========================================================================== */
function showToast(message) {
  let toast = document.getElementById('toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toast';
    toast.className = 'toast';
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 2200);
}

/* ==========================================================================
   2. Theme Toggle System (Light Mode Default, User-Switchable Dark Mode)
   ========================================================================== */
function initThemeToggle() {
  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    try {
      localStorage.setItem('theme', theme);
    } catch (e) {}
    window.dispatchEvent(new CustomEvent('themeChanged', { detail: { theme: theme } }));
  }

  // Ensure initial theme is synced
  let savedTheme = 'light';
  try {
    savedTheme = localStorage.getItem('theme') || 'light';
  } catch (e) {}

  if (savedTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
  } else {
    document.documentElement.setAttribute('data-theme', 'light');
  }

  // Event delegation: intercepts ANY .theme-toggle-btn clicked anywhere
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.theme-toggle-btn');
    if (!btn) return;
    e.preventDefault();
    e.stopPropagation();

    const isCurrentDark = document.documentElement.getAttribute('data-theme') === 'dark';
    const nextTheme = isCurrentDark ? 'light' : 'dark';
    applyTheme(nextTheme);

    showToast(nextTheme === 'dark' ? 'Switched to Dark Mode 🌙' : 'Switched to Light Mode ☀️');
  });
}

/* ==========================================================================
   3. Mobile Navigation Drawer
   ========================================================================== */
function initMobileNav() {
  const toggleBtn = document.getElementById('mobile-menu-toggle');
  const drawer = document.getElementById('mobile-nav-drawer');
  if (!toggleBtn || !drawer) return;

  const iconMenu = toggleBtn.querySelector('.icon-menu');
  const iconClose = toggleBtn.querySelector('.icon-close');

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isOpen = drawer.classList.toggle('open');
    toggleBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    drawer.setAttribute('aria-hidden', isOpen ? 'false' : 'true');

    if (iconMenu && iconClose) {
      iconMenu.style.display = isOpen ? 'none' : 'block';
      iconClose.style.display = isOpen ? 'block' : 'none';
    }
  });

  // Close when clicking outside drawer
  document.addEventListener('click', (e) => {
    if (drawer.classList.contains('open') && !drawer.contains(e.target) && !toggleBtn.contains(e.target)) {
      drawer.classList.remove('open');
      toggleBtn.setAttribute('aria-expanded', 'false');
      drawer.setAttribute('aria-hidden', 'true');
      if (iconMenu && iconClose) {
        iconMenu.style.display = 'block';
        iconClose.style.display = 'none';
      }
    }
  });

  // Close when clicking any navigation link
  drawer.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      drawer.classList.remove('open');
      toggleBtn.setAttribute('aria-expanded', 'false');
      drawer.setAttribute('aria-hidden', 'true');
      if (iconMenu && iconClose) {
        iconMenu.style.display = 'block';
        iconClose.style.display = 'none';
      }
    });
  });
}

/* ==========================================================================
   4. Global Site Search Engine (CmdK / Search Bar Modal)
   ========================================================================== */
async function loadSearchIndex() {
  if (isSearchIndexLoaded && siteSearchIndex.length > 0) return siteSearchIndex;
  try {
    const res = await fetch('/data/search-index.json');
    if (res.ok) {
      siteSearchIndex = await res.json();
      isSearchIndexLoaded = true;
      const countEl = document.getElementById('search-match-count');
      if (countEl) countEl.textContent = `${siteSearchIndex.length} topics indexed`;
    }
  } catch (err) {
    console.warn('Failed to load search index:', err);
  }
  return siteSearchIndex;
}

function initGlobalSiteSearch() {
  // Preload search index in background
  if ('requestIdleCallback' in window) {
    window.requestIdleCallback(() => loadSearchIndex());
  } else {
    setTimeout(loadSearchIndex, 500);
  }

  // Ensure modal DOM element exists
  let modal = document.getElementById('site-search-modal');
  if (!modal) {
    modal = createSearchModalDOM();
    document.body.appendChild(modal);
  }

  function getModalElements() {
    const m = document.getElementById('site-search-modal') || modal;
    return {
      modal: m,
      input: m.querySelector('#modal-search-input'),
      clearBtn: m.querySelector('#modal-search-clear'),
      closeBtn: m.querySelector('#modal-close-btn'),
      results: m.querySelector('#modal-search-results'),
      tabs: m.querySelectorAll('.filter-tab')
    };
  }

  function openSearchModal(initialQuery = '') {
    loadSearchIndex();
    const els = getModalElements();
    els.modal.classList.add('open');
    els.modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    if (els.input) {
      if (initialQuery) {
        els.input.value = initialQuery;
        if (els.clearBtn) els.clearBtn.style.display = 'flex';
        performSearch(initialQuery);
      } else {
        els.input.value = '';
        if (els.clearBtn) els.clearBtn.style.display = 'none';
        renderQuickSuggestions(els.results);
      }

      setTimeout(() => {
        els.input.focus();
        if (initialQuery) els.input.select();
      }, 60);
    }
  }

  function closeSearchModal() {
    const els = getModalElements();
    els.modal.classList.remove('open');
    els.modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  // Event delegation: Intercept ANY search trigger button clicked across the whole page
  document.addEventListener('click', (e) => {
    const trigger = e.target.closest('.search-trigger-btn');
    if (trigger) {
      e.preventDefault();
      openSearchModal();
    }
  });

  // Global Keyboard Shortcuts (Ctrl+K, Cmd+K, or '/')
  document.addEventListener('keydown', (e) => {
    const els = getModalElements();
    const isOpen = els.modal.classList.contains('open');

    // Ctrl+K or Cmd+K
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (isOpen) {
        closeSearchModal();
      } else {
        openSearchModal();
      }
      return;
    }

    // Forward slash '/' when not in input or textarea
    if (e.key === '/' && !isOpen) {
      const activeTag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
      if (activeTag !== 'input' && activeTag !== 'textarea' && !document.activeElement.isContentEditable) {
        e.preventDefault();
        openSearchModal();
        return;
      }
    }

    // Escape to close
    if (e.key === 'Escape' && isOpen) {
      e.preventDefault();
      closeSearchModal();
      return;
    }

    // Arrow navigation inside open modal
    if (isOpen) {
      if (e.key === 'ArrowDown') {
        e.preventDefault();
        navigateResults(1);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        navigateResults(-1);
      } else if (e.key === 'Enter') {
        if (selectedResultIndex >= 0 && currentResults[selectedResultIndex]) {
          e.preventDefault();
          window.location.href = currentResults[selectedResultIndex].url;
        }
      }
    }
  });

  // Modal close handlers
  const els = getModalElements();
  if (els.closeBtn) els.closeBtn.addEventListener('click', closeSearchModal);
  els.modal.addEventListener('click', (e) => {
    if (e.target === els.modal) closeSearchModal();
  });

  // Real-time input searching
  if (els.input) {
    els.input.addEventListener('input', (e) => {
      const q = e.target.value.trim();
      if (els.clearBtn) els.clearBtn.style.display = q ? 'flex' : 'none';
      if (!q) {
        renderQuickSuggestions(els.results);
      } else {
        performSearch(q);
      }
    });
  }

  // Clear button
  if (els.clearBtn) {
    els.clearBtn.addEventListener('click', () => {
      if (els.input) {
        els.input.value = '';
        els.input.focus();
      }
      els.clearBtn.style.display = 'none';
      renderQuickSuggestions(els.results);
    });
  }

  // Filter tabs
  els.tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      els.tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      activeSearchFilter = tab.getAttribute('data-filter') || 'all';
      const q = els.input ? els.input.value.trim() : '';
      if (!q) {
        renderQuickSuggestions(els.results);
      } else {
        performSearch(q);
      }
    });
  });

  // Expose global opener function
  window.openRouterIPHubSearch = openSearchModal;
}

function createSearchModalDOM() {
  const modal = document.createElement('div');
  modal.id = 'site-search-modal';
  modal.className = 'search-modal-backdrop';
  modal.setAttribute('aria-hidden', 'true');
  modal.setAttribute('role', 'dialog');
  modal.setAttribute('aria-modal', 'true');

  modal.innerHTML = `
    <div class="search-modal-container">
      <div class="search-modal-header">
        <svg class="search-modal-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input 
          type="search" 
          id="modal-search-input" 
          class="modal-search-input" 
          placeholder="Search 150+ models, default IPs, tools, guides... (e.g. 192.168.1.1, Archer, Wi-Fi QR, hard reset)" 
          autocomplete="off" 
          spellcheck="false"
        >
        <button id="modal-search-clear" class="modal-search-clear" aria-label="Clear search" style="display: none;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
        <kbd class="modal-close-kbd" id="modal-close-btn" title="Close search (Esc)">ESC</kbd>
      </div>

      <div class="search-filter-tabs">
        <button class="filter-tab active" data-filter="all">All Topics</button>
        <button class="filter-tab" data-filter="Router Model">📡 Routers</button>
        <button class="filter-tab" data-filter="ISP Gateway">🏢 ISP</button>
        <button class="filter-tab" data-filter="Gateway IP">⚡ Gateway IPs</button>
        <button class="filter-tab" data-filter="Brand Directory">🏷️ Brands</button>
        <button class="filter-tab" data-filter="Interactive Tool">🛠️ Tools</button>
        <button class="filter-tab" data-filter="Setup Guide">📖 Guides</button>
      </div>

      <div id="modal-search-results" class="search-results-list" role="listbox"></div>

      <div class="search-modal-footer">
        <div class="search-footer-hint">
          <span><kbd>&uarr;</kbd> <kbd>&darr;</kbd> to navigate</span>
          <span><kbd>&crarr;</kbd> to open</span>
          <span><kbd>ESC</kbd> to close</span>
        </div>
        <span id="search-match-count" class="search-match-count">160+ topics indexed</span>
      </div>
    </div>
  `;
  return modal;
}

function performSearch(query) {
  const container = document.getElementById('modal-search-results');
  if (!container) return;

  if (!siteSearchIndex.length) {
    container.innerHTML = `
      <div class="search-empty-state">
        <div class="search-empty-icon">⏳</div>
        <div class="search-empty-title">Loading search database...</div>
      </div>
    `;
    loadSearchIndex().then(() => performSearch(query));
    return;
  }

  const q = query.toLowerCase().trim();
  const tokens = q.split(/\s+/).filter(t => t.length > 0);

  let filtered = siteSearchIndex.filter(item => {
    if (activeSearchFilter !== 'all' && item.category !== activeSearchFilter) {
      return false;
    }

    const titleLower = (item.title || '').toLowerCase();
    const snippetLower = (item.snippet || item.description || '').toLowerCase();
    const keywordsLower = Array.isArray(item.keywords)
      ? item.keywords.join(' ').toLowerCase()
      : (item.keywords || '').toLowerCase();
    const badgeLower = (item.badge || '').toLowerCase();

    // All search tokens must appear somewhere
    return tokens.every(token => 
      titleLower.includes(token) || 
      snippetLower.includes(token) || 
      keywordsLower.includes(token) ||
      badgeLower.includes(token)
    );
  });

  // Relevance ranking
  filtered.sort((a, b) => {
    let scoreA = 0;
    let scoreB = 0;

    const titleA = (a.title || '').toLowerCase();
    const titleB = (b.title || '').toLowerCase();
    const badgeA = (a.badge || '').toLowerCase();
    const badgeB = (b.badge || '').toLowerCase();

    // Exact matches
    if (titleA === q || badgeA === q) scoreA += 100;
    if (titleB === q || badgeB === q) scoreB += 100;

    // Starts with query
    if (titleA.startsWith(q) || badgeA.startsWith(q)) scoreA += 60;
    if (titleB.startsWith(q) || badgeB.startsWith(q)) scoreB += 60;

    // Full query in title
    if (titleA.includes(q)) scoreA += 40;
    if (titleB.includes(q)) scoreB += 40;

    // Utility boosts
    if (a.category === 'Interactive Tool' || a.category === 'Setup Guide') scoreA += 20;
    if (b.category === 'Interactive Tool' || b.category === 'Setup Guide') scoreB += 20;

    // Token occurrences
    tokens.forEach(t => {
      if (titleA.includes(t)) scoreA += 15;
      if (titleB.includes(t)) scoreB += 15;
    });

    return scoreB - scoreA;
  });

  currentResults = filtered.slice(0, 20);
  selectedResultIndex = currentResults.length > 0 ? 0 : -1;

  if (currentResults.length === 0) {
    container.innerHTML = `
      <div class="search-empty-state">
        <div class="search-empty-icon">🔍</div>
        <div class="search-empty-title">No matching results for "${escapeHtml(query)}"</div>
        <div class="search-empty-desc">
          Try searching for a gateway IP (e.g. <code>192.168.1.1</code>), router model (e.g. <code>Nighthawk</code>, <code>Archer</code>), tool (<code>Wi-Fi QR</code>, <code>subnet</code>), or guide (<code>hard reset</code>, <code>bridge mode</code>).
        </div>
      </div>
    `;
    return;
  }

  renderResultsList(currentResults, query, container);
}

function renderResultsList(items, query, container) {
  container.innerHTML = items.map((item, idx) => {
    const isSelected = idx === selectedResultIndex ? ' selected' : '';
    const highlightedTitle = highlightSearchMatches(item.title, query);
    const highlightedSnippet = highlightSearchMatches(item.snippet || item.description || '', query);

    return `
      <a href="${item.url}" class="search-result-item${isSelected}" data-index="${idx}">
        <div class="search-result-main">
          <div class="search-result-top">
            <span class="search-result-badge">${escapeHtml(item.badge || item.category)}</span>
            <div class="search-result-title">${highlightedTitle}</div>
          </div>
          <div class="search-result-snippet">${highlightedSnippet}</div>
        </div>
        <div class="search-result-arrow">&rarr;</div>
      </a>
    `;
  }).join('');

  // Mouse hover synchronization
  container.querySelectorAll('.search-result-item').forEach(el => {
    el.addEventListener('mouseenter', () => {
      const idx = parseInt(el.getAttribute('data-index'), 10);
      selectedResultIndex = idx;
      updateSelectedVisual(container);
    });
  });
}

function renderQuickSuggestions(container) {
  if (!container) return;
  currentResults = [];
  selectedResultIndex = -1;

  container.innerHTML = `
    <div class="search-suggestions-header">🔥 Popular Topics & Quick Tools</div>
    <div class="search-chips-wrap">
      <a href="/tools/wifi-qr-code/" class="search-chip">🛠️ Wi-Fi QR Code Generator</a>
      <a href="/tools/subnet-calculator/" class="search-chip">🛠️ Subnet CIDR Calculator</a>
      <a href="/tools/detect-gateway/" class="search-chip">⚡ Auto-Detect My Gateway IP</a>
      <a href="/howto.html#wifi7-setup" class="search-chip">📖 Wi-Fi 7 (320 MHz) Setup</a>
      <a href="/howto.html#hard-reset" class="search-chip">📖 30-30-30 Hard Reset Guide</a>
      <a href="/ip/192-168-1-1/" class="search-chip">⚡ 192.168.1.1 (Netgear / ASUS)</a>
      <a href="/ip/192-168-0-1/" class="search-chip">⚡ 192.168.0.1 (TP-Link / D-Link)</a>
      <a href="/ip/10-0-0-1/" class="search-chip">⚡ 10.0.0.1 (Xfinity Comcast)</a>
      <a href="/ip/192-168-1-254/" class="search-chip">⚡ 192.168.1.254 (AT&T Fiber)</a>
      <a href="/isp/xfinity-xfi/" class="search-chip">🏢 Xfinity xFi Gateway</a>
      <a href="/isp/att-bgw320/" class="search-chip">🏢 AT&T BGW320 Fiber</a>
    </div>

    <div class="search-suggestions-header">📡 Popular Hardware Models</div>
    <div class="search-chips-wrap">
      <a href="/routers/netgear-nighthawk-rax50/" class="search-chip">Netgear Nighthawk RAX50</a>
      <a href="/routers/tp-link-archer-ax55/" class="search-chip">TP-Link Archer AX55</a>
      <a href="/routers/asus-rt-ax88u/" class="search-chip">ASUS RT-AX88U</a>
      <a href="/routers/ubiquiti-unifi-dream-machine-pro/" class="search-chip">UniFi Dream Machine Pro</a>
      <a href="/routers/amazon-eero-pro-6e/" class="search-chip">Amazon Eero Pro 6E</a>
    </div>
  `;
}

function navigateResults(direction) {
  if (currentResults.length === 0) return;
  const container = document.getElementById('modal-search-results');
  if (!container) return;

  selectedResultIndex += direction;
  if (selectedResultIndex < 0) selectedResultIndex = currentResults.length - 1;
  if (selectedResultIndex >= currentResults.length) selectedResultIndex = 0;

  updateSelectedVisual(container);

  const selectedEl = container.querySelector(`.search-result-item[data-index="${selectedResultIndex}"]`);
  if (selectedEl) {
    selectedEl.scrollIntoView({ block: 'nearest' });
  }
}

function updateSelectedVisual(container) {
  container.querySelectorAll('.search-result-item').forEach(el => {
    const idx = parseInt(el.getAttribute('data-index'), 10);
    if (idx === selectedResultIndex) {
      el.classList.add('selected');
    } else {
      el.classList.remove('selected');
    }
  });
}

function highlightSearchMatches(text, query) {
  if (!text) return '';
  if (!query) return escapeHtml(text);

  const tokens = query.trim().split(/\s+/).filter(t => t.length > 0);
  if (tokens.length === 0) return escapeHtml(text);

  const regex = new RegExp(`(${tokens.map(escapeRegExp).join('|')})`, 'gi');
  const escapedText = escapeHtml(text);

  return escapedText.replace(regex, '<mark class="search-highlight">$1</mark>');
}

function escapeRegExp(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

/* ==========================================================================
   5. Interactive Copy Buttons (Event Delegation)
   ========================================================================== */
function initCopyButtons() {
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.copy-btn');
    if (!btn) return;
    e.preventDefault();

    const textToCopy = btn.getAttribute('data-copy');
    if (!textToCopy) return;

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast(`Copied to clipboard: ${textToCopy}`);
      }).catch(() => {
        fallbackCopy(textToCopy);
      });
    } else {
      fallbackCopy(textToCopy);
    }
  });
}

function fallbackCopy(text) {
  const textarea = document.createElement('textarea');
  textarea.value = text;
  textarea.style.position = 'fixed';
  textarea.style.opacity = '0';
  document.body.appendChild(textarea);
  textarea.focus();
  textarea.select();
  try {
    document.execCommand('copy');
    showToast(`Copied to clipboard: ${text}`);
  } catch (err) {
    showToast('Failed to copy. Please select manually.');
  }
  document.body.removeChild(textarea);
}

/* ==========================================================================
   6. Homepage Router Table Search (#router-search)
   ========================================================================== */
async function initSearch() {
  const searchInput = document.getElementById('router-search');
  const tableBody = document.getElementById('router-table-body');
  const countEl = document.getElementById('search-count');

  if (!searchInput || !tableBody) return;

  try {
    const res = await fetch('/data/routers.json');
    if (res.ok) {
      routersData = await res.json();
    }
  } catch (err) {
    console.warn('Local data fetch failed, using pre-rendered table rows.');
  }

  searchInput.addEventListener('input', (e) => {
    const query = e.target.value.trim().toLowerCase();

    if (!routersData || !routersData.length) {
      // Fallback: filter existing static table rows
      const rows = tableBody.querySelectorAll('tr');
      let visible = 0;
      rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        if (text.includes(query)) {
          row.style.display = '';
          visible++;
        } else {
          row.style.display = 'none';
        }
      });
      if (countEl) countEl.textContent = `Showing ${visible} router models`;
      return;
    }

    // Dynamic filtering supporting all schema variants
    const filtered = routersData.filter(item => {
      const brand = (item.brand || '').toLowerCase();
      const model = (item.model_name || item.model || '').toLowerCase();
      const ip = (item.default_ip || item.ip || '').toLowerCase();
      const user = (item.default_username || item.username || '').toLowerCase();
      const pass = (item.default_password || item.password || '').toLowerCase();
      const notes = (item.notes || item.hardware_type || '').toLowerCase();

      return (
        brand.includes(query) ||
        model.includes(query) ||
        ip.includes(query) ||
        user.includes(query) ||
        pass.includes(query) ||
        notes.includes(query)
      );
    });

    renderTableRows(filtered, tableBody);
    if (countEl) countEl.textContent = `Showing ${filtered.length} of ${routersData.length} models`;

    updateTableSearchHint(query, filtered.length);
  });
}

function updateTableSearchHint(query, matchCount) {
  let hintBanner = document.getElementById('table-search-hint');
  if (!query) {
    if (hintBanner) hintBanner.remove();
    return;
  }

  const isToolOrGuideQuery = ['reset', 'qr', 'password', 'dns', 'port', 'double nat', 'windows', 'mac', 'iphone', 'subnet'].some(term => query.includes(term));

  if (matchCount === 0 || isToolOrGuideQuery) {
    if (!hintBanner) {
      hintBanner = document.createElement('div');
      hintBanner.id = 'table-search-hint';
      hintBanner.className = 'table-search-hint-banner';
      const searchWrap = document.querySelector('.search-toolbar');
      if (searchWrap && searchWrap.parentNode) {
        searchWrap.parentNode.insertBefore(hintBanner, searchWrap.nextSibling);
      }
    }
    hintBanner.innerHTML = `
      <span>💡 Looking for setup guides, diagnostic tools, or terminal commands?</span>
      <a onclick="window.openRouterIPHubSearch('${escapeHtml(query)}')">
        Search entire site for "${escapeHtml(query)}" &rarr;
      </a>
    `;
  } else if (hintBanner) {
    hintBanner.remove();
  }
}

function renderTableRows(items, container) {
  if (items.length === 0) {
    container.innerHTML = `
      <tr>
        <td colspan="5" style="text-align: center; padding: 2.5rem 1rem; color: var(--text-muted);">
          No matching router models found in hardware database.
          <div style="margin-top: 0.75rem;">
            <button class="search-trigger-btn btn btn-primary" style="display: inline-flex; margin: 0 auto; font-size: 0.85rem;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              <span>Search All Guides, Tools & Diagnostics</span>
            </button>
          </div>
        </td>
      </tr>
    `;
    return;
  }

  container.innerHTML = items.map(item => {
    const brand = item.brand || '';
    const model = item.model_name || item.model || '';
    const ip = item.default_ip || item.ip || '';
    const web = item.web_domain || item.webAddress || '';
    const user = item.default_username || item.username || '';
    const pass = item.default_password || item.password || '';
    const notes = item.notes || item.hardware_type || '';

    return `
    <tr>
      <td class="cell-brand">
        ${escapeHtml(brand)}
        <div style="font-size: 0.8rem; font-weight: normal; color: var(--text-muted);">${escapeHtml(model)}</div>
      </td>
      <td>
        <div style="display: flex; align-items: center; gap: 0.5rem;">
          <a href="http://${escapeHtml(ip)}" target="_blank" rel="noopener noreferrer" class="cell-code">
            ${escapeHtml(ip)}
          </a>
          <button class="copy-btn" data-copy="${escapeHtml(ip)}" title="Copy IP" aria-label="Copy IP ${escapeHtml(ip)}">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          </button>
        </div>
        ${web ? `<div style="font-size: 0.775rem; color: var(--text-muted); margin-top: 0.2rem;">${escapeHtml(web)}</div>` : ''}
      </td>
      <td>
        <span class="cell-code">${escapeHtml(user)}</span>
        <button class="copy-btn" data-copy="${escapeHtml(user)}" title="Copy username" aria-label="Copy username">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
        </button>
      </td>
      <td>
        <span class="cell-code">${escapeHtml(pass)}</span>
        <button class="copy-btn" data-copy="${escapeHtml(pass)}" title="Copy password" aria-label="Copy password">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
        </button>
      </td>
      <td style="font-size: 0.85rem; color: var(--text-secondary); max-width: 280px;">
        ${escapeHtml(notes)}
      </td>
    </tr>
  `;
  }).join('');
}

function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

/* ==========================================================================
   7. FAQ Accordion Support
   ========================================================================= */
function initFaqAccordion() {
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const answer = btn.nextElementSibling;
      if (!answer) return;
      const isExpanded = btn.getAttribute('aria-expanded') === 'true';

      btn.setAttribute('aria-expanded', !isExpanded);
      answer.style.display = isExpanded ? 'none' : 'block';
    });
  });
}

/* ==========================================================================
   8. Instant Speculative Link Prefetching
   ========================================================================== */
function initInstantPrefetch() {
  document.querySelectorAll('a[href^="/"]').forEach(link => {
    link.addEventListener('mouseenter', () => {
      const href = link.getAttribute('href');
      if (href && !href.startsWith('#') && !document.querySelector(`link[rel="prefetch"][href="${href}"]`)) {
        const prefetch = document.createElement('link');
        prefetch.rel = 'prefetch';
        prefetch.href = href;
        document.head.appendChild(prefetch);
      }
    }, { passive: true });
  });
}
