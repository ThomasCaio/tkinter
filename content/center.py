def center(window):
    """Função para centralizar janelas."""
    window.update_idletasks()
    winx = window.winfo_width()
    winy = window.winfo_height()
    x = int((window.winfo_screenwidth() // 2) - (winx // 2))
    y = int((window.winfo_screenheight() // 2) - (winy // 2))
    window.geometry("{}x{}+{}+{}".format(winx, winy, x, y))