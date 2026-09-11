(() => {
  const host = (location.hostname || "").replace(/^www\./, "");
  if (!host || host === "localhost") return;

  const d = new Date();
  const pad = (n) => String(n).padStart(2, "0");
  const today = `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;

  chrome.storage.local.get({ checks: {} }, (res) => {
    const checks = res.checks || {};
    checks[host] = checks[host] || {};
    checks[host][today] = (checks[host][today] || 0) + 1;
    chrome.storage.local.set({ checks });
  });
})();