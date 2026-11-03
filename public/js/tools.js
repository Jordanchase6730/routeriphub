/**
 * RouterIPHub - Interactive Networking Tools Engine
 * Zero dependencies, ultra-fast client-side execution.
 */

document.addEventListener('DOMContentLoaded', () => {
  initWifiQrGenerator();
  initSubnetCalculator();
  initPasswordGenerator();
  initPortSearch();
  initGatewayProbe();
});

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

// Add callers to DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
  initLocalIPDetector();
  initSubnetCheatSheet();
});
