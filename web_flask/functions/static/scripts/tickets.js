const API_URL_BASE = 'http://localhost:5001/api/endpoints'
const url = `${API_URL_BASE}/admin/tickets`

const status_class = {
	null: {msg: 'No Asignado', cls: 'is-danger'},
	0: {msg: 'No Asignado', cls: 'is-danger'},
	1: {msg: 'Asignado', cls: 'is-info'},
	2: {msg: 'Completado', cls: 'is-success'}
}

$(document).ready(() => {
	$('.table-container .table tbody').html('')
	$.get(url, (res) => {
		res.forEach((el, ind) => {
			const status = status_class[el.Status]

			$('.table-container .table tbody').append(`
				<tr>
					<th>${'$n'.replace('$n', ind + 1).padStart(4, '0')}</th>
					<td>${el.id}</td>
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
	})
})

