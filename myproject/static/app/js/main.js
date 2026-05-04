(function () {
  const state = {
    keyboardHandlers: {},
    currentPage: null,
  };

  function registerShortcut(scope, handler) {
    unregisterShortcut(scope);
    state.keyboardHandlers[scope] = handler;
    window.addEventListener("keydown", handler);
  }

  function unregisterShortcut(scope) {
    const existing = state.keyboardHandlers[scope];
    if (existing) {
      window.removeEventListener("keydown", existing);
      delete state.keyboardHandlers[scope];
    }
  }

  async function api(path, options = {}) {
    const response = await fetch(path, options);
    if (!response.ok) {
      const text = await response.text();
      throw new Error(text || `${response.status} ${response.statusText}`);
    }
    if (response.status === 204) return null;
    return response.json();
  }

  window.HoopTrackApp = {
    state,
    api,
    registerShortcut,
    unregisterShortcut,
  };
})();
