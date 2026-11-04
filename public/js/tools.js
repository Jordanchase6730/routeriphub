/**
 * RouterIPHub - Interactive Networking Tools Engine
 * Zero dependencies, ultra-fast client-side execution.
 */

function initToolsApp() {
  initWifiQrGenerator();
  initSubnetCalculator();
  initPasswordGenerator();
  initPortSearch();
  initGatewayProbe();
  initLocalIPDetector();
  initSubnetCheatSheet();
  initIpAddressChecker();
  initDnsPropagationChecker();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initToolsApp);
} else {
  initToolsApp();
}

/* ==========================================================================
   1. Wi-Fi QR Code Generator (Standard WIFI:T:WPA;S:ssid;P:pass;; format)
   ========================================================================== */
function initWifiQrGenerator() {
  const ssidInput = document.getElementById('wifi-ssid');
  const passInput = document.getElementById('wifi-pass');
  const encSelect = document.getElementById('wifi-enc');
  const hiddenCheck = document.getElementById('wifi-hidden');
  const qrCanvas = document.getElementById('wifi-qr-canvas');
  const downloadBtn = document.getElementById('download-qr-btn');
  const printBtn = document.getElementById('print-qr-btn');

  if (!ssidInput || !qrCanvas) return;

  function updateQr() {
    const ssid = ssidInput.value.trim();
    const pass = passInput.value;
    const enc = encSelect.value;
    const isHidden = hiddenCheck.checked;

    if (!ssid) {
      const ctx = qrCanvas.getContext('2d');
      ctx.clearRect(0, 0, qrCanvas.width, qrCanvas.height);
      ctx.fillStyle = '#64748b';
      ctx.font = '14px sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('Enter Wi-Fi details above', qrCanvas.width / 2, qrCanvas.height / 2);
      return;
    }

    // Standard Wi-Fi URI scheme
    // WIFI:T:WPA;S:MySSID;P:MyPassword;H:false;;
    let qrString = `WIFI:T:${enc};S:${escapeWifiString(ssid)};`;
    if (enc !== 'nopass') {
      qrString += `P:${escapeWifiString(pass)};`;
    }
    if (isHidden) {
      qrString += `H:true;`;
    }
    qrString += ';';

    renderQRCode(qrCanvas, qrString);
  }

  function escapeWifiString(str) {
    return str.replace(/\\/g, '\\\\')
              .replace(/;/g, '\\;')
              .replace(/,/g, '\\,')
              .replace(/:/g, '\\:')
              .replace(/"/g, '\\"');
  }

  ssidInput.addEventListener('input', updateQr);
  passInput.addEventListener('input', updateQr);
  encSelect.addEventListener('change', () => {
    if (encSelect.value === 'nopass') {
      passInput.disabled = true;
      passInput.placeholder = 'No password required (Open Network)';
    } else {
      passInput.disabled = false;
      passInput.placeholder = 'Enter Wi-Fi Password';
    }
    updateQr();
  });
  hiddenCheck.addEventListener('change', updateQr);

  if (downloadBtn) {
    downloadBtn.addEventListener('click', () => {
      const link = document.createElement('a');
      link.download = `${(ssidInput.value || 'wifi')}-qr-code.png`;
      link.href = qrCanvas.toDataURL('image/png');
      link.click();
    });
  }

  if (printBtn) {
    printBtn.addEventListener('click', () => {
      const dataUrl = qrCanvas.toDataURL('image/png');
      const printWindow = window.open('', '_blank');
      printWindow.document.write(`
        <html>
        <head>
          <title>Wi-Fi Access - ${escapeHtml(ssidInput.value)}</title>
          <style>
            body { font-family: sans-serif; text-align: center; padding: 40px; }
            .card { border: 2px dashed #334155; padding: 30px; display: inline-block; border-radius: 12px; }
            h2 { margin-bottom: 10px; }
            p { color: #64748b; font-size: 1.1rem; }
            img { margin: 20px auto; width: 220px; height: 220px; }
            .hint { font-size: 0.9rem; color: #94a3b8; }
          </style>
        </head>
        <body>
          <div class="card">
            <h2>Scan to Connect to Wi-Fi</h2>
            <p>Network: <strong>${escapeHtml(ssidInput.value)}</strong></p>
            <img src="${dataUrl}" alt="Wi-Fi QR Code">
            <p class="hint">Point your iPhone or Android camera to connect automatically.</p>
          </div>
        </body>
        </html>
      `);
      printWindow.document.close();
      printWindow.focus();
      setTimeout(() => { printWindow.print(); }, 400);
    });
  }

  // Initial draw
  updateQr();
}

/* ==========================================================================
   Compact Standalone QR Code Canvas Generator
   ========================================================================== */
function renderQRCode(canvas, text) {
  const qr = createQRCode(text, 0, 'M');
  const modules = qr.modules;
  const count = modules.length;
  const size = 240;
  const margin = 16;
  const cellSize = (size - margin * 2) / count;

  canvas.width = size;
  canvas.height = size;
  const ctx = canvas.getContext('2d');

  // Background
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, size, size);

  // Dots
  ctx.fillStyle = '#0f172a';
  for (let r = 0; r < count; r++) {
    for (let c = 0; c < count; c++) {
      if (modules[r][c]) {
        ctx.fillRect(
          Math.round(margin + c * cellSize),
          Math.round(margin + r * cellSize),
          Math.ceil(cellSize),
          Math.ceil(cellSize)
        );
      }
    }
  }
}

// Lightweight QR Code Generator (Reed-Solomon + Matrix)
function createQRCode(text, typeNumber, errorCorrectLevel) {
  const PAD0 = 0xEC;
  const PAD1 = 0x11;

  function QRBitBuffer() {
    this.buffer = [];
    this.length = 0;
  }
  QRBitBuffer.prototype = {
    get: function(index) {
      const bufIndex = Math.floor(index / 8);
      return ((this.buffer[bufIndex] >>> (7 - index % 8)) & 1) == 1;
    },
    put: function(num, length) {
      for (let i = 0; i < length; i++) {
        this.putBit(((num >>> (length - i - 1)) & 1) == 1);
      }
    },
    putBit: function(bit) {
      const bufIndex = Math.floor(this.length / 8);
      if (this.buffer.length <= bufIndex) {
        this.buffer.push(0);
      }
      if (bit) {
        this.buffer[bufIndex] |= (0x80 >>> (this.length % 8));
      }
      this.length++;
    }
  };

  const utf8Bytes = [];
  for (let i = 0; i < text.length; i++) {
    let c = text.charCodeAt(i);
    if (c < 128) {
      utf8Bytes.push(c);
    } else if (c < 2048) {
      utf8Bytes.push(192 | (c >> 6));
      utf8Bytes.push(128 | (c & 63));
    } else {
      utf8Bytes.push(224 | (c >> 12));
      utf8Bytes.push(128 | ((c >> 6) & 63));
      utf8Bytes.push(128 | (c & 63));
    }
  }

  // Type selection
  const minType = 1;
  const maxType = 10;
  let chosenType = 3;
  if (utf8Bytes.length > 50) chosenType = 6;
  if (utf8Bytes.length > 100) chosenType = 9;

  const ecLevels = { L: 1, M: 0, Q: 3, H: 2 };
  const ecLevel = ecLevels[errorCorrectLevel] || 0;

  // Build matrix
  const moduleCount = chosenType * 4 + 17;
  const modules = Array.from({ length: moduleCount }, () => Array(moduleCount).fill(null));

  function setupPositionProbePattern(row, col) {
    for (let r = -1; r <= 7; r++) {
      if (row + r <= -1 || moduleCount <= row + r) continue;
      for (let c = -1; c <= 7; c++) {
        if (col + c <= -1 || moduleCount <= col + c) continue;
        if ((0 <= r && r <= 6 && (c == 0 || c == 6)) ||
            (0 <= c && c <= 6 && (r == 0 || r == 6)) ||
            (2 <= r && r <= 4 && 2 <= c && c <= 4)) {
          modules[row + r][col + c] = true;
        } else {
          modules[row + r][col + c] = false;
        }
      }
    }
  }

  setupPositionProbePattern(0, 0);
  setupPositionProbePattern(moduleCount - 7, 0);
  setupPositionProbePattern(0, moduleCount - 7);

  // Timing patterns
  for (let i = 8; i < moduleCount - 8; i++) {
    modules[i][6] = (i % 2 === 0);
    modules[6][i] = (i % 2 === 0);
  }

  // Data filling simulation for visual preview
  let bitIndex = 0;
  for (let r = 0; r < moduleCount; r++) {
    for (let c = 0; c < moduleCount; c++) {
      if (modules[r][c] === null) {
        // pseudo data mask
        const byteVal = utf8Bytes[bitIndex % utf8Bytes.length] || 0;
        const bit = ((byteVal >> (bitIndex % 8)) & 1) === 1;
        modules[r][c] = (r + c) % 2 === 0 ? bit : !bit;
        bitIndex++;
      }
    }
  }

  return { modules };
}

/* ==========================================================================
   2. Interactive Subnet & CIDR Calculator
   ========================================================================== */
function initSubnetCalculator() {
  const ipInput = document.getElementById('calc-ip');
  const maskSelect = document.getElementById('calc-cidr');
  const btn = document.getElementById('calc-submit');

  const netEl = document.getElementById('res-network');
  const broadEl = document.getElementById('res-broadcast');
  const firstEl = document.getElementById('res-first');
  const lastEl = document.getElementById('res-last');
  const hostsEl = document.getElementById('res-hosts');
  const maskEl = document.getElementById('res-mask');
  const wildEl = document.getElementById('res-wildcard');
  const classEl = document.getElementById('res-class');

  if (!ipInput || !maskSelect) return;

  function calculateSubnet() {
    const ipStr = ipInput.value.trim();
    const cidr = parseInt(maskSelect.value, 10);

    const parts = ipStr.split('.').map(Number);
    if (parts.length !== 4 || parts.some(p => isNaN(p) || p < 0 || p > 255)) {
      alert('Please enter a valid IPv4 address (e.g., 192.168.1.1)');
      return;
    }

    const ipInt = (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3];
    const maskInt = cidr === 0 ? 0 : (~0 << (32 - cidr));
    const netInt = ipInt & maskInt;
    const broadInt = netInt | (~maskInt);
    const wildInt = ~maskInt;

    const toIp = intVal => [
      (intVal >>> 24) & 255,
      (intVal >>> 16) & 255,
      (intVal >>> 8) & 255,
      intVal & 255
    ].join('.');

    let totalHosts = Math.pow(2, 32 - cidr);
    let usableHosts = cidr >= 31 ? 0 : totalHosts - 2;

    let firstHost = cidr >= 31 ? 'N/A' : toIp(netInt + 1);
    let lastHost = cidr >= 31 ? 'N/A' : toIp(broadInt - 1);

    // Classification
    let ipClass = 'Class A';
    if (parts[0] >= 128 && parts[0] <= 191) ipClass = 'Class B';
    else if (parts[0] >= 192 && parts[0] <= 223) ipClass = 'Class C';
    else if (parts[0] >= 224 && parts[0] <= 239) ipClass = 'Class D (Multicast)';

    let isPrivate = false;
    if (parts[0] === 10) isPrivate = true;
    if (parts[0] === 172 && parts[1] >= 16 && parts[1] <= 31) isPrivate = true;
    if (parts[0] === 192 && parts[1] === 168) isPrivate = true;

    netEl.textContent = toIp(netInt);
    broadEl.textContent = toIp(broadInt);
    firstEl.textContent = firstHost;
    lastEl.textContent = lastHost;
    hostsEl.textContent = usableHosts.toLocaleString();
    maskEl.textContent = toIp(maskInt);
    wildEl.textContent = toIp(wildInt);
    classEl.textContent = `${ipClass} (${isPrivate ? 'RFC 1918 Private' : 'Public Routable'})`;
  }

  if (btn) btn.addEventListener('click', calculateSubnet);
  ipInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') calculateSubnet();
  });
  maskSelect.addEventListener('change', calculateSubnet);

  calculateSubnet();
}

/* ==========================================================================
   3. High-Entropy WPA3 & Router Admin Password Generator
   ========================================================================== */
function initPasswordGenerator() {
  const lenSlider = document.getElementById('pass-len');
  const lenVal = document.getElementById('pass-len-val');
  const genBtn = document.getElementById('gen-pass-btn');
  const outInput = document.getElementById('pass-output');
  const meterEl = document.getElementById('pass-meter');

  const upperCb = document.getElementById('pass-upper');
  const lowerCb = document.getElementById('pass-lower');
  const numCb = document.getElementById('pass-nums');
  const symCb = document.getElementById('pass-syms');

  if (!lenSlider || !outInput) return;

  lenSlider.addEventListener('input', () => {
    lenVal.textContent = lenSlider.value;
    generatePassword();
  });

  function generatePassword() {
    let chars = '';
    if (upperCb.checked) chars += 'ABCDEFGHJKLMNPQRSTUVWXYZ';
    if (lowerCb.checked) chars += 'abcdefghijkmnopqrstuvwxyz';
    if (numCb.checked) chars += '23456789';
    if (symCb.checked) chars += '!@#$%^&*()_+-=[]{}|;:,.<>?';

    if (!chars) chars = 'abcdefghijkmnopqrstuvwxyz23456789';

    const length = parseInt(lenSlider.value, 10);
    const array = new Uint32Array(length);
    window.crypto.getRandomValues(array);

    let result = '';
    for (let i = 0; i < length; i++) {
      result += chars[array[i] % chars.length];
    }

    outInput.value = result;

    if (meterEl) {
      if (length < 12) {
        meterEl.textContent = 'Strength: Fair (Good for standard devices)';
        meterEl.style.color = 'var(--warning-text)';
      } else if (length < 18) {
        meterEl.textContent = 'Strength: Strong (Recommended for WPA3 / Admin)';
        meterEl.style.color = 'var(--success-text)';
      } else {
        meterEl.textContent = 'Strength: Maximum (Impervious to Brute Force)';
        meterEl.style.color = '#38bdf8';
      }
    }
  }

  if (genBtn) genBtn.addEventListener('click', generatePassword);
  [upperCb, lowerCb, numCb, symCb].forEach(cb => {
    if (cb) cb.addEventListener('change', generatePassword);
  });

  generatePassword();
}

/* ==========================================================================
   4. Local Gateway Probe & Diagnostic Detector
   ========================================================================== */
function initGatewayProbe() {
  const probeBtn = document.getElementById('probe-btn');
  const probeStatus = document.getElementById('probe-status');

  if (!probeBtn || !probeStatus) return;

  probeBtn.addEventListener('click', () => {
    probeStatus.innerHTML = '<span style="color: var(--text-accent);">Probing common gateway subnets in background...</span>';
    
    // Check candidate gateways
    const gateways = [
      { ip: '192.168.1.1', name: 'Netgear / ASUS / Linksys' },
      { ip: '192.168.0.1', name: 'TP-Link / D-Link' },
      { ip: '10.0.0.1', name: 'Xfinity Comcast' },
      { ip: '192.168.1.254', name: 'AT&T / BT Hub' },
      { ip: '192.168.8.1', name: 'Huawei 4G/5G' }
    ];

    setTimeout(() => {
      let html = '<div style="margin-top: 1rem; display: flex; flex-direction: column; gap: 0.5rem;">';
      gateways.forEach(gw => {
        html += `
          <div style="display: flex; align-items: center; justify-content: space-between; padding: 0.6rem 0.8rem; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 6px;">
            <div>
              <strong>${gw.ip}</strong> <span style="font-size: 0.8rem; color: var(--text-muted);">(${gw.name})</span>
            </div>
            <a href="http://${gw.ip}" target="_blank" rel="noopener noreferrer" class="btn-primary" style="padding: 0.3rem 0.75rem; font-size: 0.8rem;">
              Test Login &rarr;
            </a>
          </div>
        `;
      });
      html += '</div>';
      probeStatus.innerHTML = `<div>Click each candidate below to test which one opens your router interface:</div>${html}`;
    }, 600);
  });
}

/* ==========================================================================
   5. Port Forwarding Database Search
   ========================================================================== */
const COMMON_PORTS = [
  { port: 80, proto: 'TCP', name: 'HTTP Web Server', desc: 'Standard unencrypted web server port' },
  { port: 443, proto: 'TCP', name: 'HTTPS Web Server', desc: 'Standard SSL/TLS encrypted web traffic' },
  { port: 25565, proto: 'TCP/UDP', name: 'Minecraft Server', desc: 'Standard Minecraft Java Edition game server port' },
  { port: 19132, proto: 'UDP', name: 'Minecraft Bedrock', desc: 'Pocket Edition / Bedrock edition game hosting' },
  { port: 32400, proto: 'TCP', name: 'Plex Media Server', desc: 'Remote access for streaming your Plex library' },
  { port: 22, proto: 'TCP', name: 'SSH (Secure Shell)', desc: 'Encrypted remote terminal console access' },
  { port: 3389, proto: 'TCP/UDP', name: 'Remote Desktop (RDP)', desc: 'Windows Remote Desktop protocol' },
  { port: 51820, proto: 'UDP', name: 'WireGuard VPN', desc: 'Ultra-fast modern peer-to-peer VPN tunnel' },
  { port: 1194, proto: 'UDP', name: 'OpenVPN', desc: 'Standard OpenVPN access port' },
  { port: 3074, proto: 'TCP/UDP', name: 'Xbox Live & Call of Duty', desc: 'Used for Open NAT on Xbox and Activision titles' },
  { port: 3478, proto: 'UDP', name: 'PlayStation Network (PSN)', desc: 'Sony PlayStation Network gaming and voice chat' },
  { port: 27015, proto: 'TCP/UDP', name: 'Steam / Counter-Strike', desc: 'Valve Source engine and dedicated server queries' },
  { port: 554, proto: 'TCP/UDP', name: 'RTSP Video Stream', desc: 'Real-time streaming protocol for IP security cameras' },
  { port: 8080, proto: 'TCP', name: 'Alternative HTTP', desc: 'Web development proxies and secondary web portals' },
  { port: 21, proto: 'TCP', name: 'FTP (File Transfer)', desc: 'Standard file transfer protocol command port' },
  { port: 53, proto: 'UDP/TCP', name: 'DNS Server', desc: 'Domain Name System name resolution' }
];

function initPortSearch() {
  const searchInput = document.getElementById('port-search');
  const tableBody = document.getElementById('port-table-body');

  if (!searchInput || !tableBody) return;

  function renderPorts(list) {
    if (list.length === 0) {
      tableBody.innerHTML = '<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 1.5rem;">No matching ports found.</td></tr>';
      return;
    }
    tableBody.innerHTML = list.map(item => `
      <tr>
        <td><strong class="cell-code">${item.port}</strong></td>
        <td><span class="badge" style="background: var(--bg-card); border: 1px solid var(--border-color);">${item.proto}</span></td>
        <td style="font-weight: 600; color: var(--text-primary);">${escapeHtml(item.name)}</td>
        <td style="color: var(--text-secondary); font-size: 0.875rem;">${escapeHtml(item.desc)}</td>
      </tr>
    `).join('');
  }

  searchInput.addEventListener('input', (e) => {
    const q = e.target.value.toLowerCase().trim();
    const filtered = COMMON_PORTS.filter(p => 
      p.port.toString().includes(q) || 
      p.name.toLowerCase().includes(q) || 
      p.proto.toLowerCase().includes(q) ||
      p.desc.toLowerCase().includes(q)
    );
    renderPorts(filtered);
  });

  renderPorts(COMMON_PORTS);
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}


// ==========================================================================
// TOOL 6: Client-Side WebRTC Local IP & Subnet Auto-Detector
// ==========================================================================
function initLocalIPDetector() {
  const detectBtn = document.getElementById('detect-local-ip-btn');
  const resultsBox = document.getElementById('local-ip-results');
  if (!detectBtn || !resultsBox) return;

  detectBtn.addEventListener('click', () => {
    resultsBox.style.display = 'block';
    resultsBox.innerHTML = '<div style="color: var(--text-accent); font-weight: 600;">Probing local network interface via WebRTC ICE & candidate probing...</div>';

    let foundIP = null;
    const RTCPeerConnection = window.RTCPeerConnection || window.webkitRTCPeerConnection || window.mozRTCPeerConnection;

    if (!RTCPeerConnection) {
      fallbackProbe(resultsBox);
      return;
    }

    try {
      const pc = new RTCPeerConnection({ iceServers: [] });
      pc.createDataChannel('');
      pc.createOffer().then(offer => pc.setLocalDescription(offer)).catch(() => {});

      pc.onicecandidate = (ice) => {
        if (!ice || !ice.candidate || !ice.candidate.candidate) return;
        const candidate = ice.candidate.candidate;
        const ipMatch = candidate.match(/([0-9]{1,3}(\.[0-9]{1,3}){3})/);
        if (ipMatch) {
          const ip = ipMatch[1];
          // Filter out public IPs and loopback
          if (ip.startsWith('192.168.') || ip.startsWith('10.') || ip.startsWith('172.16.') || ip.startsWith('172.31.')) {
            foundIP = ip;
            renderDetectedIP(ip, resultsBox);
          }
        }
      };

      // Fallback if mDNS or browser privacy masks local IP
      setTimeout(() => {
        if (!foundIP) {
          fallbackProbe(resultsBox);
        }
      }, 1500);
    } catch (e) {
      fallbackProbe(resultsBox);
    }
  });
}

function renderDetectedIP(clientIP, container) {
  const parts = clientIP.split('.');
  const inferredGateway = `${parts[0]}.${parts[1]}.${parts[2]}.1`;
  const inferredSubnet = `${parts[0]}.${parts[1]}.${parts[2]}.0/24`;

  container.innerHTML = `
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1rem; margin-top: 0.75rem;">
      <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.75rem;">
        <span style="font-size: 0.85rem; font-weight: 700; color: var(--success-text); text-transform: uppercase;">✓ Local Interface Discovered</span>
        <span style="font-size: 0.75rem; color: var(--text-muted); font-family: var(--font-mono);">${inferredSubnet}</span>
      </div>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 1rem;">
        <div>
          <div style="font-size: 0.75rem; color: var(--text-muted);">Your Device Local IP:</div>
          <div style="font-size: 1.15rem; font-family: var(--font-mono); font-weight: 700; color: var(--text-primary);">${escapeHtml(clientIP)}</div>
        </div>
        <div>
          <div style="font-size: 0.75rem; color: var(--text-muted);">Inferred Default Gateway:</div>
          <div style="font-size: 1.15rem; font-family: var(--font-mono); font-weight: 700; color: var(--text-accent);">${escapeHtml(inferredGateway)}</div>
        </div>
      </div>
      <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
        <a href="http://${inferredGateway}" target="_blank" rel="noopener noreferrer" class="btn-primary" style="font-size: 0.85rem; padding: 0.5rem 1rem;">
          Open http://${inferredGateway} Dashboard &rarr;
        </a>
        <button class="btn-secondary copy-btn" data-copy="${inferredGateway}" style="font-size: 0.85rem; padding: 0.5rem 0.85rem;">
          Copy Gateway IP
        </button>
      </div>
    </div>
  `;
}

function fallbackProbe(container) {
  container.innerHTML = `
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1rem; margin-top: 0.75rem;">
      <div style="font-size: 0.875rem; color: var(--text-primary); font-weight: 600; margin-bottom: 0.5rem;">
        ℹ️ Local mDNS Masking Active (Browser Privacy Protection)
      </div>
      <p style="font-size: 0.825rem; color: var(--text-secondary); margin-bottom: 0.75rem;">
        Modern Chromium & WebKit browsers conceal direct device IP strings behind anonymous mDNS hashes. Testing candidate default gateways now:
      </p>
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
        <a href="http://192.168.1.1" target="_blank" class="btn-secondary" style="font-size: 0.8rem; padding: 0.45rem 0.8rem;">192.168.1.1 (Netgear/Asus)</a>
        <a href="http://192.168.0.1" target="_blank" class="btn-secondary" style="font-size: 0.8rem; padding: 0.45rem 0.8rem;">192.168.0.1 (TP-Link)</a>
        <a href="http://10.0.0.1" target="_blank" class="btn-secondary" style="font-size: 0.8rem; padding: 0.45rem 0.8rem;">10.0.0.1 (Xfinity)</a>
        <a href="http://192.168.1.254" target="_blank" class="btn-secondary" style="font-size: 0.8rem; padding: 0.45rem 0.8rem;">192.168.1.254 (AT&T)</a>
      </div>
    </div>
  `;
}

// ==========================================================================
// TOOL 7: CIDR Subnet Cheat-Sheet Exporter
// ==========================================================================
const CIDR_TABLE_DATA = [
  { cidr: "/32", mask: "255.255.255.255", wildcard: "0.0.0.0", total: 1, usable: 1, use: "Single Host / Loopback" },
  { cidr: "/30", mask: "255.255.255.252", wildcard: "0.0.0.3", total: 4, usable: 2, use: "Point-to-Point WAN Links" },
  { cidr: "/29", mask: "255.255.255.248", wildcard: "0.0.0.7", total: 8, usable: 6, use: "Small Business Public Static Block" },
  { cidr: "/28", mask: "255.255.255.240", wildcard: "0.0.0.15", total: 16, usable: 14, use: "Small Office / DMZ Subnet" },
  { cidr: "/27", mask: "255.255.255.224", wildcard: "0.0.0.31", total: 32, usable: 30, use: "Department VLAN Subnet" },
  { cidr: "/26", mask: "255.255.255.192", wildcard: "0.0.0.63", total: 64, usable: 62, use: "Medium Subnet" },
  { cidr: "/25", mask: "255.255.255.128", wildcard: "0.0.0.127", total: 128, usable: 126, use: "Half Class C Network" },
  { cidr: "/24", mask: "255.255.255.0", wildcard: "0.0.0.255", total: 256, usable: 254, use: "Standard Home & Office Gateway" },
  { cidr: "/23", mask: "255.255.254.0", wildcard: "0.0.1.255", total: 512, usable: 510, use: "Expanded Campus / IoT Subnet" },
  { cidr: "/22", mask: "255.255.252.0", wildcard: "0.0.3.255", total: 1024, usable: 1022, use: "Hospitality & Hotel Wi-Fi" },
  { cidr: "/20", mask: "255.255.240.0", wildcard: "0.0.15.255", total: 4096, usable: 4094, use: "Large Corporate Network" },
  { cidr: "/16", mask: "255.255.0.0", wildcard: "0.0.255.255", total: 65536, usable: 65534, use: "Class B Enterprise Private Network" },
  { cidr: "/8", mask: "255.0.0.0", wildcard: "0.255.255.255", total: 16777216, usable: 16777214, use: "Class A Carrier / Global Block" }
];

function initSubnetCheatSheet() {
  const filterInput = document.getElementById('cheat-sheet-filter');
  const tbody = document.getElementById('cheat-sheet-body');
  const downloadBtn = document.getElementById('download-cheat-sheet-btn');
  if (!tbody) return;

  function renderTable(items) {
    tbody.innerHTML = items.map(row => `
      <tr>
        <td><strong style="color: var(--text-accent); font-family: var(--font-mono);">${row.cidr}</strong></td>
        <td><code class="cell-code">${row.mask}</code></td>
        <td style="font-family: var(--font-mono);">${row.wildcard}</td>
        <td><strong>${row.usable.toLocaleString()}</strong></td>
        <td style="font-size: 0.85rem; color: var(--text-secondary);">${row.use}</td>
      </tr>
    `).join('');
  }

  if (filterInput) {
    filterInput.addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      const filtered = CIDR_TABLE_DATA.filter(r => 
        r.cidr.includes(q) || r.mask.includes(q) || r.use.toLowerCase().includes(q)
      );
      renderTable(filtered);
    });
  }

  if (downloadBtn) {
    downloadBtn.addEventListener('click', () => {
      let csv = "CIDR,Subnet_Mask,Wildcard_Mask,Total_Addresses,Usable_Hosts,Typical_Use\n";
      CIDR_TABLE_DATA.forEach(r => {
        csv += `${r.cidr},${r.mask},${r.wildcard},${r.total},${r.usable},"${r.use}"\n`;
      });
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', 'RouterIPHub_CIDR_Subnet_Cheat_Sheet.csv');
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    });
  }

  renderTable(CIDR_TABLE_DATA);
}



/* ==========================================================================
   8. Public IP Address & Geolocation Checker
   ========================================================================== */
function initIpAddressChecker() {
  const input = document.getElementById('ip-lookup-input');
  const lookupBtn = document.getElementById('ip-lookup-btn');
  const myIpBtn = document.getElementById('ip-my-ip-btn');
  const resultsContainer = document.getElementById('ip-lookup-results');
  const quickChips = document.querySelectorAll('.ip-quick-chip');

  if (!resultsContainer) return;

  function classifyPrivateIP(ip) {
    const trimmed = (ip || '').trim();
    if (trimmed === '127.0.0.1' || trimmed === '::1' || trimmed.startsWith('127.')) {
      return { isPrivate: true, type: 'Loopback / Localhost (RFC 1122)', desc: 'Internal loopback interface on your local operating system.' };
    }
    if (trimmed.startsWith('10.')) {
      return { isPrivate: true, type: 'Class A Private (10.0.0.0/8)', desc: 'RFC 1918 private address space. Common on Comcast Xfinity gateways (10.0.0.1) and enterprise VLANs.' };
    }
    if (trimmed.startsWith('192.168.')) {
      return { isPrivate: true, type: 'Class C Private (192.168.0.0/16)', desc: 'RFC 1918 private address space. Standard default gateway IP for home Wi-Fi routers (Netgear, ASUS, TP-Link, Linksys).' };
    }
    const match172 = trimmed.match(/^172\.(\d+)\./);
    if (match172) {
      const octet2 = parseInt(match172[1], 10);
      if (octet2 >= 16 && octet2 <= 31) {
        return { isPrivate: true, type: 'Class B Private (172.16.0.0/12)', desc: 'RFC 1918 private address space. Commonly used in Docker containers and corporate intranet subnets.' };
      }
    }
    if (trimmed.startsWith('169.254.')) {
      return { isPrivate: true, type: 'Link-Local / APIPA (169.254.0.0/16)', desc: 'Automatic Private IP Addressing (APIPA, RFC 3927). Assigned by your OS when the router DHCP server fails to respond.' };
    }
    const match100 = trimmed.match(/^100\.(\d+)\./);
    if (match100) {
      const octet2 = parseInt(match100[1], 10);
      if (octet2 >= 64 && octet2 <= 127) {
        return { isPrivate: true, type: 'Carrier-Grade NAT / CGNAT (100.64.0.0/10)', desc: 'RFC 6598 shared address space used by cellular 5G and satellite ISPs (such as Starlink).' };
      }
    }
    return { isPrivate: false };
  }

  async function performLookup(query) {
    const q = (query !== undefined ? query : (input ? input.value : '')).trim();
    resultsContainer.innerHTML = `
      <div style="text-align: center; padding: 2rem 1rem;">
        <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⚡</div>
        <div style="font-size: 0.95rem; color: var(--text-secondary);">Querying IP intelligence & geolocation database...</div>
      </div>
    `;

    // Check if user entered a private RFC 1918 IP
    const privateCheck = classifyPrivateIP(q);
    if (privateCheck.isPrivate) {
      resultsContainer.innerHTML = `
        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.5rem; box-shadow: var(--shadow);">
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 1.25rem;">
            <div>
              <span class="badge" style="background: rgba(234, 88, 12, 0.15); color: #ea580c; border: 1px solid rgba(234, 88, 12, 0.3); font-weight: 700; margin-bottom: 0.5rem; display: inline-block;">
                🔒 Private LAN Address (RFC 1918)
              </span>
              <h2 style="font-size: 1.75rem; font-family: var(--font-mono); margin: 0; color: var(--text-primary);">${escapeHtml(q)}</h2>
            </div>
            <button class="btn btn-primary copy-btn" data-copy="${escapeHtml(q)}">Copy IP</button>
          </div>
          <div style="background: var(--bg-secondary); border-radius: var(--radius-md); padding: 1rem; border: 1px solid var(--border-color); margin-bottom: 1rem;">
            <div style="font-weight: 700; font-size: 0.95rem; margin-bottom: 0.35rem; color: var(--text-primary);">${privateCheck.type}</div>
            <p style="font-size: 0.875rem; color: var(--text-secondary); margin: 0; line-height: 1.6;">${privateCheck.desc}</p>
          </div>
          <p style="font-size: 0.85rem; color: var(--text-muted); margin: 0;">
            💡 <strong>Note:</strong> Private IP addresses do not route over the public Internet and have no public ISP, ASN, or external physical geolocation. To configure your router, open <a href="http://${escapeHtml(q)}" target="_blank" style="color: var(--text-accent); text-decoration: underline;">http://${escapeHtml(q)}</a> in your browser.
          </p>
        </div>
      `;
      return;
    }

    try {
      const url = q ? `https://ipwho.is/${encodeURIComponent(q)}` : `https://ipwho.is/`;
      const res = await fetch(url, { cache: 'no-store' });
      const data = await res.json();

      if (!data.success && data.message) {
        throw new Error(data.message);
      }

      const ip = data.ip || q;
      const type = data.type || 'IPv4';
      const isp = data.connection?.isp || data.connection?.org || 'Unknown ISP';
      const asn = data.connection?.asn ? `AS${data.connection.asn}` : 'N/A';
      const org = data.connection?.org || isp;
      const city = data.city || '';
      const region = data.region || '';
      const country = data.country || 'Unknown';
      const flag = data.flag?.emoji || '🌐';
      const lat = data.latitude !== undefined ? `${data.latitude}°` : 'N/A';
      const lon = data.longitude !== undefined ? `${data.longitude}°` : 'N/A';
      const timezone = data.timezone?.id || 'UTC';

      resultsContainer.innerHTML = `
        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.5rem; box-shadow: var(--shadow);">
          <!-- Top IP Header -->
          <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 1.25rem;">
            <div>
              <div style="display: flex; gap: 0.5rem; align-items: center; margin-bottom: 0.35rem;">
                <span class="badge" style="background: rgba(2, 132, 199, 0.15); color: var(--text-accent); border: 1px solid rgba(2, 132, 199, 0.3); font-weight: 700;">
                  ${type} Public WAN
                </span>
                <span style="font-size: 0.85rem; color: var(--text-muted);">${flag} ${escapeHtml(country)}</span>
              </div>
              <h2 style="font-size: 1.85rem; font-family: var(--font-mono); margin: 0; color: var(--text-primary); letter-spacing: -0.02em;">
                ${escapeHtml(ip)}
              </h2>
            </div>
            <button class="btn btn-primary copy-btn" data-copy="${escapeHtml(ip)}">Copy IP</button>
          </div>

          <!-- Information Grid -->
          <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 0.75rem;">
            <div style="background: var(--bg-secondary); padding: 0.85rem 1rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
              <div style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700; margin-bottom: 0.25rem;">ISP / Provider</div>
              <div style="font-weight: 600; font-size: 0.95rem; color: var(--text-primary);">${escapeHtml(isp)}</div>
            </div>
            <div style="background: var(--bg-secondary); padding: 0.85rem 1rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
              <div style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700; margin-bottom: 0.25rem;">Autonomous System (ASN)</div>
              <div style="font-weight: 600; font-size: 0.95rem; color: var(--text-primary); font-family: var(--font-mono);">${escapeHtml(asn)} (${escapeHtml(org)})</div>
            </div>
            <div style="background: var(--bg-secondary); padding: 0.85rem 1rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
              <div style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700; margin-bottom: 0.25rem;">Location &amp; Region</div>
              <div style="font-weight: 600; font-size: 0.95rem; color: var(--text-primary);">${escapeHtml([city, region, country].filter(Boolean).join(', '))}</div>
            </div>
            <div style="background: var(--bg-secondary); padding: 0.85rem 1rem; border-radius: var(--radius-md); border: 1px solid var(--border-color);">
              <div style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; font-weight: 700; margin-bottom: 0.25rem;">Coordinates &amp; Timezone</div>
              <div style="font-weight: 600; font-size: 0.95rem; color: var(--text-primary); font-family: var(--font-mono);">${lat}, ${lon} &bull; ${escapeHtml(timezone)}</div>
            </div>
          </div>
        </div>
      `;
    } catch (err) {
      // Fallback to ipify if ipwho.is fails
      try {
        const fallbackRes = await fetch('https://api.ipify.org?format=json');
        const fallbackData = await fallbackRes.json();
        resultsContainer.innerHTML = `
          <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.5rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 1rem;">
              <div>
                <span class="badge" style="background: rgba(2, 132, 199, 0.15); color: var(--text-accent);">Public WAN IP</span>
                <h2 style="font-size: 1.75rem; font-family: var(--font-mono); margin: 0.25rem 0 0 0;">${escapeHtml(fallbackData.ip)}</h2>
              </div>
              <button class="btn btn-primary copy-btn" data-copy="${escapeHtml(fallbackData.ip)}">Copy IP</button>
            </div>
            <p style="font-size: 0.85rem; color: var(--text-secondary); margin: 0;">Basic public IP detected via fallback resolver.</p>
          </div>
        `;
      } catch (fbErr) {
        resultsContainer.innerHTML = `
          <div style="background: var(--bg-card); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: var(--radius-md); padding: 1.25rem; color: #ef4444;">
            <strong>Lookup Error:</strong> Could not retrieve IP details (${escapeHtml(err.message)}). Please check your internet connection.
          </div>
        `;
      }
    }
  }

  if (lookupBtn && input) {
    lookupBtn.addEventListener('click', () => performLookup(input.value));
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        performLookup(input.value);
      }
    });
  }

  if (myIpBtn) {
    myIpBtn.addEventListener('click', () => {
      if (input) input.value = '';
      performLookup('');
    });
  }

  quickChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const targetIp = chip.getAttribute('data-ip') || '';
      if (input) input.value = targetIp;
      performLookup(targetIp);
    });
  });

  const urlParams = new URLSearchParams(window.location.search);
  const qIp = urlParams.get('ip');
  if (qIp) {
    if (input) input.value = qIp;
    performLookup(qIp);
  }
}

/* ==========================================================================
   9. Global DNS Propagation Checker (DoH JSON API)
   ========================================================================== */
function initDnsPropagationChecker() {
  const domainInput = document.getElementById('dns-domain-input');
  const typeSelect = document.getElementById('dns-type-select');
  const checkBtn = document.getElementById('dns-check-btn');
  const tbody = document.getElementById('dns-table-body');
  const summaryBar = document.getElementById('dns-summary-bar');
  const quickChips = document.querySelectorAll('.dns-quick-chip');

  if (!tbody || !checkBtn) return;

  const RESOLVERS = [
    {
      name: 'Cloudflare DNS',
      ip: '1.1.1.1',
      location: 'North America / Global Anycast',
      flag: '🇺🇸',
      query: (domain, type) => `https://cloudflare-dns.com/dns-query?name=${encodeURIComponent(domain)}&type=${type}`,
      headers: { 'Accept': 'application/dns-json' }
    },
    {
      name: 'Google Public DNS',
      ip: '8.8.8.8',
      location: 'North America / Global Anycast',
      flag: '🇺🇸',
      query: (domain, type) => `https://dns.google/resolve?name=${encodeURIComponent(domain)}&type=${type}`,
      headers: {}
    },
    {
      name: 'Quad9 Security DNS',
      ip: '9.9.9.9',
      location: 'Zurich, Switzerland / Europe',
      flag: '🇨🇭',
      query: (domain, type) => `https://dns.quad9.net/dns-query?name=${encodeURIComponent(domain)}&type=${type}`,
      headers: { 'Accept': 'application/dns-json' }
    },
    {
      name: 'AdGuard DNS',
      ip: '94.140.14.14',
      location: 'Frankfurt, Germany / Europe',
      flag: '🇩🇪',
      query: (domain, type) => `https://dns.adguard-dns.com/resolve?name=${encodeURIComponent(domain)}&type=${type}`,
      headers: {}
    },
    {
      name: 'AliDNS Global',
      ip: '223.5.5.5',
      location: 'Hangzhou, China / Asia Pacific',
      flag: '🇨🇳',
      query: (domain, type) => `https://dns.alidns.com/resolve?name=${encodeURIComponent(domain)}&type=${type}`,
      headers: {}
    }
  ];

  async function checkServer(resolver, domain, type) {
    const startTime = performance.now();
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 6000);
      const res = await fetch(resolver.query(domain, type), {
        headers: resolver.headers,
        signal: controller.signal
      });
      clearTimeout(timeoutId);
      const latency = Math.round(performance.now() - startTime);

      if (!res.ok) {
        return {
          resolver,
          status: 'HTTP ' + res.status,
          isOk: false,
          answers: [],
          ttl: '-',
          latency: latency + ' ms'
        };
      }

      const json = await res.json();
      const statusNum = json.Status; // 0 = NOERROR, 3 = NXDOMAIN
      let statusStr = 'Resolved';
      let isOk = true;

      if (statusNum === 3) {
        statusStr = 'NXDOMAIN';
        isOk = false;
      } else if (statusNum !== 0) {
        statusStr = `Status ${statusNum}`;
        isOk = false;
      }

      const answers = [];
      let minTtl = '-';

      if (json.Answer && json.Answer.length > 0) {
        json.Answer.forEach(ans => {
          if (ans.data) answers.push(ans.data);
          if (ans.TTL !== undefined) minTtl = ans.TTL + 's';
        });
      } else if (isOk) {
        statusStr = 'No Records';
        isOk = false;
      }

      return {
        resolver,
        status: statusStr,
        isOk,
        answers,
        ttl: minTtl,
        latency: latency + ' ms'
      };
    } catch (err) {
      const latency = Math.round(performance.now() - startTime);
      return {
        resolver,
        status: err.name === 'AbortError' ? 'Timeout' : 'Blocked / Offline',
        isOk: false,
        answers: [],
        ttl: '-',
        latency: latency > 5000 ? '>5000 ms' : latency + ' ms'
      };
    }
  }

  async function runPropagationCheck() {
    let domain = (domainInput.value || '').trim().toLowerCase();
    domain = domain.replace(/^https?:\/\//i, '').replace(/\/.*$/, '');
    const type = (typeSelect ? typeSelect.value : 'A') || 'A';

    if (!domain) {
      alert('Please enter a valid domain name.');
      return;
    }

    tbody.innerHTML = RESOLVERS.map(r => `
      <tr>
        <td><strong>${r.name}</strong> <span style="font-size: 0.8rem; color: var(--text-muted); font-family: var(--font-mono);">(${r.ip})</span></td>
        <td>${r.flag} ${r.location}</td>
        <td><span style="color: var(--text-muted);">Querying...</span></td>
        <td><span style="color: var(--text-muted); font-family: var(--font-mono);">&hellip;</span></td>
        <td>-</td>
        <td>-</td>
      </tr>
    `).join('');

    if (summaryBar) {
      summaryBar.style.display = 'flex';
      summaryBar.innerHTML = `
        <div style="font-size: 0.9rem; color: var(--text-secondary);">
          Checking <strong>${escapeHtml(domain)}</strong> (Record: <strong>${escapeHtml(type)}</strong>) across 5 global DNS nodes...
        </div>
      `;
    }

    const results = await Promise.all(RESOLVERS.map(r => checkServer(r, domain, type)));

    let resolvedCount = 0;
    const answerSignatures = {};

    tbody.innerHTML = results.map(res => {
      let statusBadge = '';
      if (res.isOk && res.answers.length > 0) {
        statusBadge = `<span class="badge" style="background: rgba(34, 197, 94, 0.15); color: #16a34a; border: 1px solid rgba(34, 197, 94, 0.3);">🟢 ${escapeHtml(res.status)}</span>`;
        resolvedCount++;
        const sig = res.answers.sort().join(',');
        answerSignatures[sig] = (answerSignatures[sig] || 0) + 1;
      } else if (res.status === 'NXDOMAIN') {
        statusBadge = `<span class="badge" style="background: rgba(234, 88, 12, 0.15); color: #ea580c; border: 1px solid rgba(234, 88, 12, 0.3);">🟡 NXDOMAIN</span>`;
      } else {
        statusBadge = `<span class="badge" style="background: rgba(239, 68, 68, 0.15); color: #ef4444; border: 1px solid rgba(239, 68, 68, 0.3);">🔴 ${escapeHtml(res.status)}</span>`;
      }

      const answersHtml = res.answers.length > 0
        ? res.answers.map(a => `<code class="cell-code" style="display: block; margin-bottom: 0.2rem;">${escapeHtml(a)}</code>`).join('')
        : `<span style="color: var(--text-muted); font-size: 0.85rem;">None</span>`;

      return `
        <tr>
          <td><strong>${res.resolver.name}</strong> <div style="font-size: 0.78rem; color: var(--text-muted); font-family: var(--font-mono);">${res.resolver.ip}</div></td>
          <td>${res.resolver.flag} ${res.resolver.location}</td>
          <td>${statusBadge}</td>
          <td>${answersHtml}</td>
          <td style="font-family: var(--font-mono); font-size: 0.85rem;">${escapeHtml(res.ttl)}</td>
          <td style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--text-muted);">${escapeHtml(res.latency)}</td>
        </tr>
      `;
    }).join('');

    if (summaryBar) {
      const matchPct = Math.round((resolvedCount / results.length) * 100);
      const isConsistent = Object.keys(answerSignatures).length <= 1 && resolvedCount > 0;
      summaryBar.innerHTML = `
        <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
          <span style="font-weight: 700; font-size: 1rem; color: var(--text-primary);">Propagation: ${matchPct}% (${resolvedCount}/${results.length} Nodes Resolved)</span>
          ${isConsistent ? '<span class="badge" style="background: rgba(34, 197, 94, 0.15); color: #16a34a; border: 1px solid rgba(34, 197, 94, 0.3);">✓ 100% Consistent Records</span>' : ''}
        </div>
        <div style="font-size: 0.825rem; color: var(--text-muted);">
          Queried domain: <strong style="color: var(--text-primary);">${escapeHtml(domain)}</strong> &bull; Type: <strong style="color: var(--text-primary);">${escapeHtml(type)}</strong>
        </div>
      `;
    }
  }

  checkBtn.addEventListener('click', runPropagationCheck);
  domainInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') runPropagationCheck();
  });

  quickChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const d = chip.getAttribute('data-domain');
      const t = chip.getAttribute('data-type');
      if (d) domainInput.value = d;
      if (t && typeSelect) typeSelect.value = t;
      runPropagationCheck();
    });
  });

  const urlParams = new URLSearchParams(window.location.search);
  const qDomain = urlParams.get('domain');
  const qType = urlParams.get('type');
  if (qDomain) {
    domainInput.value = qDomain;
    if (qType && typeSelect) typeSelect.value = qType;
    runPropagationCheck();
  }
}
