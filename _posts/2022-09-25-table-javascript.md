---
title: Post with Table
toc: true
layout: notebook
categories: [javascript]
image: /images/groupwork_icon.jpeg
nb_path: _notebooks/2022-09-25-javascript-table.ipynb
---

```html
    <!DOCTYPE html>
    <html lang="{{ page.lang | default: site.lang | default: "en" }}">

    "include head.html"

    <body>

        "include header.html"

        <main class="page-content" aria-label="Content">
        <div class="wrapper">
            "content"
            <table>
                 <tr>
                     <th>Week</th>
                     <th>Things Done</th>
                     <th>Place</th>
                </tr>
                 <tr>
                    <td>1</td>
                    <td>3</td>
                    <td>School</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>5</td>
                    <td>School</td>
                </tr>
            </table>
        </div>
        </main>

        "include footer.html"

    </body>

    </html>
```