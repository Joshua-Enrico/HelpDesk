const API_URL_BASE = 'http://localhost:5001/api/endpoints'
const url = `${API_URL_BASE}/admin/tickets/`
let page = 1

const status_class = {
	null: {msg: 'No Asignado', cls: 'is-danger'},
	0: {msg: 'No Asignado', cls: 'is-danger'},
	1: {msg: 'Asignado', cls: 'is-info'},
	2: {msg: 'Completado', cls: 'is-success'}
}


function renderPagination(pag) {
    const prevUrl = url + pag.prev_num
    const nextUrl = url + pag.next_num
    const clickPrev = `onclick="getTickets('${prevUrl}')"`
    const clickNext = `onclick="getTickets('${nextUrl}')"`
    const paginationDOM = $('.pagination.is-rounded')

    let pagLinks = ''
    for (let i = 1; i <= pag.pages; i++)
        pagLinks += `<li>
                        <a class="pagination-link ${(i == pag.page)? 'is-current': ''}"
                           onclick="getTickets('${url + i}')"
                           aria-label="Page ${i}">
                            ${i}
                        </a>
                    </li>`

    const html = `
     <div class="pagination is-rounded" role="navigation" aria-label="pagination">
      <a class="pagination-previous" ${pag.has_prev? clickPrev: 'disabled'}>Previous</a>
      <a class="pagination-next" ${pag.has_next? clickNext: 'disabled'}>Next page</a>
      <ul class="pagination-list">
        <!--
        <li><a class="pagination-link is-current" aria-label="Goto page 1" aria-current="page">1</a></li>
        <li><span class="pagination-ellipsis">&hellip;</span></li>
        <li><a class="pagination-link" aria-label="Goto page 45">45</a></li>
        <li><a class="pagination-link" aria-label="Page 46">46</a></li>
        <li><a class="pagination-link" aria-label="Goto page 47">47</a></li>
        <li><span class="pagination-ellipsis">&hellip;</span></li>
        <li><a class="pagination-link" aria-label="Goto page 86">86</a></li>
        -->
        ${pagLinks}
      </ul>
    </div>
    `
    paginationDOM.html(html)
}


function renderTickets(tickets, page, per_page) {
    const container = $('.table-container .table tbody')
    
    const baseCount = (page - 1) * per_page
    container.html('')

	tickets.forEach((el, ind) => {
        const status = status_class[el.Status]
        container.append(`
            <tr>
                <th><input type="checkbox"></th>
                <th>${'$n'.replace('$n', baseCount + ind + 1).padStart(4, '0')}</th>
                <th>
                    <button class="button ${status.cls}">${status.msg}</button>
                </th>
                <td>${el.Subject}</td>
                <td>${el.Agent || '---'}</td>
                <td>${el.Company_Area}</td>
                <td>${(new Date(el.DateTime)).toISOString().split('T')[0].split('-').reverse().join('-')}</td>
                <td>
                    <a class="button">
                    <span class="icon is-small">
                    <i class="fa fa-ellipsis-v "></i>
                </span>
                </a>
                </td>
            </tr>`)
    })
}


function getTickets(ticketsUrl) {
    $.get(ticketsUrl, (res) => {
        renderTickets(res.items, res.page, res.per_page)
        renderPagination(res)
	})
}

$(document).ready(() => getTickets(url + 1))

