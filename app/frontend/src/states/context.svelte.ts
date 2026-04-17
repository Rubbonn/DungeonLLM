interface ContextState {
    currentPage: 'main-menu' | 'new-game' | 'load-game' | 'create-player' | 'chat-view'
}

const contextState: ContextState = $state({
    currentPage: 'chat-view'
});

export default contextState;