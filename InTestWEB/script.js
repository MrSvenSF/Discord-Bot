// Load config.json (relative path from this HTML file to config folder)
const CONFIG_PATH = '../config/config.json';

const moduleListEl = document.getElementById('module-list');
const reloadBtn = document.getElementById('reload-btn');
const saveBtn = document.getElementById('save-btn');
const downloadLink = document.getElementById('download-link');

let config = null;

async function fetchConfig() {
	const res = await fetch(CONFIG_PATH + '?_=' + Date.now());
	if (!res.ok) throw new Error('Fehler beim Laden der Konfiguration: ' + res.status);
	return await res.json();
}

function renderModules() {
	moduleListEl.innerHTML = '';
	if (!config || !Array.isArray(config.modules)) {
		moduleListEl.textContent = 'Keine Module in der Konfiguration gefunden.';
		return;
	}

	config.modules.forEach((m, idx) => {
		const row = document.createElement('div');
		row.className = 'module-row';

		const label = document.createElement('label');
		label.className = 'module-label';
		label.textContent = m.name || ('Module ' + idx);

		const toggle = document.createElement('input');
		toggle.type = 'checkbox';
		toggle.checked = !!m.enabled;
		toggle.className = 'module-toggle';
		toggle.addEventListener('change', () => {
			m.enabled = toggle.checked;
		});

		row.appendChild(label);
		row.appendChild(toggle);
		moduleListEl.appendChild(row);
	});
}

async function loadAndRender() {
	try {
		config = await fetchConfig();
		renderModules();
	} catch (err) {
		moduleListEl.textContent = err.message || String(err);
	}
}

function downloadConfig() {
	const data = JSON.stringify(config, null, 4);
	const blob = new Blob([data], { type: 'application/json' });
	const url = URL.createObjectURL(blob);
	downloadLink.href = url;
	downloadLink.download = 'config.json';
	downloadLink.style.display = 'inline';
	downloadLink.textContent = 'Download config.json';
}

reloadBtn.addEventListener('click', () => loadAndRender());
saveBtn.addEventListener('click', () => downloadConfig());

// initial load
loadAndRender();

// Allow toggling all modules on/off via keyboard shortcuts (optional):
document.addEventListener('keydown', (e) => {
	if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'a') {
		// ctrl/cmd + A -> set all enabled
		if (!config || !Array.isArray(config.modules)) return;
		const setTo = true;
		config.modules.forEach(m => m.enabled = setTo);
		renderModules();
		e.preventDefault();
	}
	if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'd') {
		// ctrl/cmd + D -> set all disabled
		if (!config || !Array.isArray(config.modules)) return;
		const setTo = false;
		config.modules.forEach(m => m.enabled = setTo);
		renderModules();
		e.preventDefault();
	}
});

// End
