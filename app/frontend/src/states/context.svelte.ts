interface ContextState {
    currentPage: 'main-menu' | 'new-game' | 'load-game' | 'create-player' | 'chat-view'
}

const contextState: ContextState = $state({
    currentPage: 'main-menu'
});

export { contextState };