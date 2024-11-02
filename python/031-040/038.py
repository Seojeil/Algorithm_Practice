# 바탕화면 정리


def solution(wallpaper):
    lux = 0
    luy = []
    rdx = 0
    rdy = []

    for w in wallpaper:
        if w == "." * len(w):
            lux += 1
        else:
            break

    for w in reversed(wallpaper):
        if w == "." * len(w):
            rdx += 1
        else:
            break

    for w in wallpaper:
        y = w.find("#")
        if y >= 0:
            luy.append(y)

    for w in wallpaper:
        w_r = w[::-1]
        y = w_r.find("#")
        if y >= 0:
            rdy.append(y)

    return [lux, min(luy), len(wallpaper) - rdx, len(wallpaper[0]) - min(rdy)]
