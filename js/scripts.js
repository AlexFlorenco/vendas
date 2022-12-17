function openPage(x, y) {
    var pagina = x
    var target = y
    var url = '../html/' + pagina + '.html'

    var xml = new XMLHttpRequest()

    xml.onreadystatechange = function () {
        if (xml.readyState == 4 && xml.status == 200) {
            document.getElementById(target).innerHTML = xml.responseText
        }
    }

    xml.open("GET", url, true)

    xml.send()
}