const API_URL_BASE = 'http://localhost:5001/api/endpoints'
const url = `${API_URL_BASE}/admin/tickets`

const status_class = {
	Asignado: {msg: 'Asignado', cls: 'is-info'},
	Completado: {msg: 'Completado', cls: 'is-success'},
	null: {msg: 'No Asignado', cls: 'is-danger'}
}

$(document).ready(() => {
	$('.table-container .table tbody').html('')
	$.get(url, (res) => {
		res.forEach((el, ind) => {
			const status = status_class[el.Status]

			$('.table-container .table tbody').append(`
				<tr>
					<th>${'$n'.replace('$n', ind + 1).padStart(4, '0')}</th>
					<th>
						<button class="button ${status.cls}">${status.msg}</button>
					</th>
					<td>${el.Subject}</td>
					<td>${el.Agent}</td>
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

