document.addEventListener("DOMContentLoaded", () => {
    fetch("/api/news")
        .then(response => response.json())
        .then(data => {
            console.log("API 回傳：", data); 
            const list = document.getElementById("news-list");
            list.innerHTML = "";

            if (!Array.isArray(data)) {
                list.innerHTML = `<li>資料格式錯誤：${JSON.stringify(data)}</li>`;
                return;
            }

            if (data.length === 0) {
                list.innerHTML = "<li>目前沒有新聞</li>";
                return;
            }

            data.forEach(news => {
                const item = document.createElement("li");
                const link = document.createElement("a");
                link.href = news.url.startsWith("http") ? news.url : `https://tw-nba.udn.com${news.url}`;
                link.textContent = news.title;
                link.target = "_blank";
                item.appendChild(link);
                list.appendChild(item);
            });
        })
        .catch(err => {
            document.getElementById("news-list").innerHTML = `<li>載入失敗：${err}</li>`;
        });
});
