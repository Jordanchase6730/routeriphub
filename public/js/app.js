/**
 * RouterIPHub - High Performance Client Engine
 * Zero dependencies, < 9KB, optimized for instant INP, global site search, theme switching, and mobile navigation.
 */

document.addEventListener('DOMContentLoaded', () => {
  initInstantSpaRouting();
  initThemeToggle();
  initMobileNav();
  initGlobalSiteSearch();
  initSearch();
  initCopyButtons();
  initFaqAccordion();
});

// Toast notification helper
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

// Theme Toggle System (Default Light, switchable to Dark)
function initThemeToggle() {
  const toggleBtns = document.querySelectorAll('.theme-toggle-btn');
  if (!toggleBtns.length) return;

  toggleBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      
      if (isDark) {
        document.documentElement.setAttribute('data-theme', 'light');
        try { localStorage.setItem('theme', 'light'); } catch (err) {}
        showToast('Switched to Light Mode');
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        try { localStorage.setItem('theme', 'dark'); } catch (err) {}
        showToast('Switched to Dark Mode');
      }

      window.dispatchEvent(new CustomEvent('themeChanged', { 
        detail: { theme: isDark ? 'light' : 'dark' } 
      }));
    });
  });
}

// Mobile Navigation Drawer
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

  // Close when clicking outside
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

  // Close when clicking any nav link inside drawer
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
   Global Site Search Engine & Modal
   ========================================================================== */
let siteSearchIndex = [];
let isSearchIndexLoaded = false;
let activeSearchFilter = 'all';
let currentResults = [];
let selectedResultIndex = -1;

async function loadSearchIndex() {
  if (isSearchIndexLoaded) return siteSearchIndex;
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
  // Preload index when browser is idle
  if ('requestIdleCallback' in window) {
    window.requestIdleCallback(() => loadSearchIndex());
  } else {
    setTimeout(loadSearchIndex, 1200);
  }

  // Ensure modal DOM element exists
  let modal = document.getElementById('site-search-modal');
  if (!modal) {
    modal = createSearchModalDOM();
    document.body.appendChild(modal);
  }

  const modalInput = document.getElementById('modal-search-input');
  const clearBtn = document.getElementById('modal-search-clear');
  const closeBtn = document.getElementById('modal-close-btn');
  const resultsContainer = document.getElementById('modal-search-results');
  const filterTabs = document.querySelectorAll('.filter-tab');

  // Open modal handlers
  function openSearchModal(initialQuery = '') {
    loadSearchIndex();
    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    if (initialQuery) {
      modalInput.value = initialQuery;
      clearBtn.style.display = 'block';
      performSearch(initialQuery);
    } else {
      modalInput.value = '';
      clearBtn.style.display = 'none';
      renderQuickSuggestions(resultsContainer);
    }

    setTimeout(() => {
      modalInput.focus();
      if (initialQuery) modalInput.select();
    }, 50);
  }

  function closeSearchModal() {
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  // Bind all search trigger buttons across the page
  document.querySelectorAll('.search-trigger-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openSearchModal();
    });
  });

  // Global Keyboard Shortcuts (Ctrl+K, Cmd+K, or '/')
  document.addEventListener('keydown', (e) => {
    // Open on Ctrl+K / Cmd+K
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      if (modal.classList.contains('open')) {
        closeSearchModal();
      } else {
        openSearchModal();
      }
      return;
    }

    // Open on '/' if user is not currently in an input/textarea
    if (e.key === '/' && !modal.classList.contains('open')) {
      const activeTag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
      if (activeTag !== 'input' && activeTag !== 'textarea' && !document.activeElement.isContentEditable) {
        e.preventDefault();
        openSearchModal();
        return;
      }
    }

    // Close on Escape if modal open
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      e.preventDefault();
      closeSearchModal();
      return;
    }

    // Arrow navigation within open search modal
    if (modal.classList.contains('open')) {
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

  // Close button & backdrop click
  if (closeBtn) closeBtn.addEventListener('click', closeSearchModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeSearchModal();
  });

  // Search input typing
  modalInput.addEventListener('input', (e) => {
    const q = e.target.value.trim();
    clearBtn.style.display = q ? 'flex' : 'none';
    if (!q) {
      renderQuickSuggestions(resultsContainer);
    } else {
      performSearch(q);
    }
  });

  // Clear button click
  clearBtn.addEventListener('click', () => {
    modalInput.value = '';
    clearBtn.style.display = 'none';
    modalInput.focus();
    renderQuickSuggestions(resultsContainer);
  });

  // Filter tabs
  filterTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      filterTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      activeSearchFilter = tab.getAttribute('data-filter') || 'all';
      const q = modalInput.value.trim();
      if (!q) {
        renderQuickSuggestions(resultsContainer);
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
          placeholder="Search 60+ routers, default IPs, tools, guides... (e.g. 192.168.1.1, Archer, Wi-Fi QR, hard reset)" 
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
        <span id="search-match-count" class="search-match-count">96 topics indexed</span>
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
    const snippetLower = (item.snippet || '').toLowerCase();
    const keywordsLower = (item.keywords || '').toLowerCase();
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

    const titleA = a.title.toLowerCase();
    const titleB = b.title.toLowerCase();
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

    // High utility boosts for interactive tools & how-to guides
    if (a.category === 'Interactive Tool' || a.category === 'Setup Guide') scoreA += 20;
    if (b.category === 'Interactive Tool' || b.category === 'Setup Guide') scoreB += 20;

    // Token occurrences in title
    tokens.forEach(t => {
      if (titleA.includes(t)) scoreA += 15;
      if (titleB.includes(t)) scoreB += 15;
    });

    return scoreB - scoreA;
  });

  currentResults = filtered.slice(0, 16);
  selectedResultIndex = currentResults.length > 0 ? 0 : -1;

  if (currentResults.length === 0) {
    container.innerHTML = `
      <div class="search-empty-state">
        <div class="search-empty-icon">🔍</div>
        <div class="search-empty-title">No matching results for "${escapeHtml(query)}"</div>
        <div class="search-empty-desc">
          Try searching for a gateway IP (e.g. <code>192.168.1.1</code>), brand (e.g. <code>Netgear</code>, <code>TP-Link</code>), tool (<code>Wi-Fi QR</code>, <code>subnet</code>), or guide (<code>hard reset</code>, <code>password</code>).
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
    const highlightedSnippet = highlightSearchMatches(item.snippet, query);

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
  currentResults = [];
  selectedResultIndex = -1;

  container.innerHTML = `
    <div class="search-suggestions-header">🔥 Popular Topics & Quick Tools</div>
    <div class="search-chips-wrap">
      <a href="/tools.html#wifi-qr" class="search-chip">🛠️ Wi-Fi QR Code Generator</a>
      <a href="/tools.html#subnet-calc" class="search-chip">🛠️ Subnet CIDR Calculator</a>
      <a href="/howto.html#hard-reset" class="search-chip">📖 30-30-30 Hard Reset</a>
      <a href="/howto.html#wifi-password" class="search-chip">📖 Change Wi-Fi Password</a>
      <a href="/192-168-1-1.html" class="search-chip">⚡ 192.168.1.1 (Netgear / ASUS)</a>
      <a href="/192-168-0-1.html" class="search-chip">⚡ 192.168.0.1 (TP-Link / D-Link)</a>
      <a href="/10-0-0-1.html" class="search-chip">⚡ 10.0.0.1 (Xfinity Comcast)</a>
      <a href="/192-168-1-254.html" class="search-chip">⚡ 192.168.1.254 (AT&T Fiber)</a>
      <a href="/find-router-ip.html#windows" class="search-chip">🔍 Find IP (Windows ipconfig)</a>
      <a href="/find-router-ip.html#mac" class="search-chip">🔍 Find IP (macOS Terminal)</a>
      <a href="/howto.html#port-forwarding" class="search-chip">🎮 Port Forwarding (Gaming/Plex)</a>
    </div>

    <div class="search-suggestions-header">⚡ Browse Gateway IP Pillars</div>
    <div class="search-chips-wrap">
      <a href="/192-168-2-1.html" class="search-chip">192.168.2.1 (Belkin)</a>
      <a href="/192-168-8-1.html" class="search-chip">192.168.8.1 (Huawei / GL.iNet)</a>
      <a href="/192-168-31-1.html" class="search-chip">192.168.31.1 (Xiaomi)</a>
      <a href="/192-168-88-1.html" class="search-chip">192.168.88.1 (MikroTik)</a>
      <a href="/192-168-100-1.html" class="search-chip">192.168.100.1 (Fiber ONT)</a>
      <a href="/192-168-12-1.html" class="search-chip">192.168.12.1 (T-Mobile 5G)</a>
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
  if (!tokens.length) return escapeHtml(text);

  let escaped = escapeHtml(text);
  tokens.forEach(tok => {
    const safe = tok.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const rx = new RegExp(`(${safe})`, 'gi');
    escaped = escaped.replace(rx, '<mark class="search-highlight">$1</mark>');
  });
  return escaped;
}

// Copy to clipboard with visual feedback
function initCopyButtons() {
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.copy-btn');
    if (!btn) return;
    
    const textToCopy = btn.getAttribute('data-copy');
    if (!textToCopy) return;

    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast(`Copied: ${textToCopy}`);
      }).catch(() => fallbackCopy(textToCopy));
    } else {
      fallbackCopy(textToCopy);
    }
  });
}

function fallbackCopy(text) {
  const textArea = document.createElement('textarea');
  textArea.value = text;
  textArea.style.position = 'fixed';
  textArea.style.left = '-999999px';
  document.body.appendChild(textArea);
  textArea.focus();
  textArea.select();
  try {
    document.execCommand('copy');
    showToast(`Copied: ${text}`);
  } catch (err) {
    showToast('Failed to copy');
  }
  document.body.removeChild(textArea);
}

// Client-side search and filtering for router table (Homepage)
let routersData = [];

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
    
    if (!routersData.length) {
      // Fallback: search existing DOM rows
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

    // Dynamic render from JSON
    const filtered = routersData.filter(item => {
      return (
        item.brand.toLowerCase().includes(query) ||
        item.model.toLowerCase().includes(query) ||
        item.ip.toLowerCase().includes(query) ||
        item.username.toLowerCase().includes(query) ||
        item.password.toLowerCase().includes(query)
      );
    });

    renderTableRows(filtered, tableBody);
    if (countEl) countEl.textContent = `Showing ${filtered.length} of ${routersData.length} models`;

    // Smart suggestion banner if 0 rows matched or if query looks like a tool/guide search
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
      const searchBox = document.querySelector('.search-box');
      if (searchBox && searchBox.parentNode) {
        searchBox.parentNode.insertBefore(hintBanner, searchBox.nextSibling);
      }
    }
    hintBanner.innerHTML = `
      <span>💡 Searching for guides, tools, or diagnostic commands?</span>
      <a onclick="window.openRouterIPHubSearch('${escapeHtml(query)}')">
        Search entire website for "${escapeHtml(query)}" &rarr;
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
            <button class="search-trigger-btn" style="display: inline-flex; margin: 0 auto;">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              <span>Search All Guides, Tools & Diagnostics</span>
            </button>
          </div>
        </td>
      </tr>
    `;
    const btn = container.querySelector('.search-trigger-btn');
    if (btn) {
      btn.addEventListener('click', () => {
        const input = document.getElementById('router-search');
        window.openRouterIPHubSearch(input ? input.value : '');
      });
    }
    return;
  }

  container.innerHTML = items.map(item => `
    <tr>
      <td class="cell-brand">
        ${escapeHtml(item.brand)}
        <div style="font-size: 0.8rem; font-weight: normal; color: var(--text-muted);">${escapeHtml(item.model)}</div>
      </td>
      <td>
        <div style="display: flex; align-items: center; gap: 0.5rem;">
          <a href="http://${escapeHtml(item.ip)}" target="_blank" rel="noopener noreferrer" class="cell-code">
            ${escapeHtml(item.ip)}
          </a>
          <button class="copy-btn" data-copy="${escapeHtml(item.ip)}" title="Copy IP" aria-label="Copy IP ${escapeHtml(item.ip)}">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
          </button>
        </div>
        ${item.webAddress ? `<div style="font-size: 0.775rem; color: var(--text-muted); margin-top: 0.2rem;">${escapeHtml(item.webAddress)}</div>` : ''}
      </td>
      <td>
        <span class="cell-code">${escapeHtml(item.username)}</span>
        <button class="copy-btn" data-copy="${escapeHtml(item.username)}" title="Copy username" aria-label="Copy username">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
        </button>
      </td>
      <td>
        <span class="cell-code">${escapeHtml(item.password)}</span>
        <button class="copy-btn" data-copy="${escapeHtml(item.password)}" title="Copy password" aria-label="Copy password">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
        </button>
      </td>
      <td style="font-size: 0.85rem; color: var(--text-secondary); max-width: 280px;">
        ${escapeHtml(item.notes)}
      </td>
    </tr>
  `).join('');
}

function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Simple FAQ Accordion with accessibility support
function initFaqAccordion() {
  const faqButtons = document.querySelectorAll('.faq-question');
  faqButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const answer = btn.nextElementSibling;
      const isExpanded = btn.getAttribute('aria-expanded') === 'true';
      
      btn.setAttribute('aria-expanded', !isExpanded);
      if (isExpanded) {
        answer.style.display = 'none';
      } else {
        answer.style.display = 'block';
      }
    });
  });
}
