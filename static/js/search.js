document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const table = document.getElementById('requestsTable');

    if (!searchInput || !table) {
        return;
    }

    const rows = table.querySelectorAll('tbody tr');
    const pagination = document.getElementById('pagination');

    searchInput.addEventListener('input', function() {
        const query = searchInput.value.trim().toLowerCase();

        if (pagination) {
            pagination.style.display = query ? 'none' : '';
        }

        rows.forEach(function (row) {
            if (row.cells.length < 3) {
                return;
            }

            const name = row.cells[0].textContent.toLowerCase();
            const phone = row.cells[1].textContent.toLowerCase();
            const email = row.cells[2].textContent.toLowerCase();

            const match = name.includes(query) || phone.includes(query) || email.includes(query);
            row.style.display = match ? '' : 'none';
        });
    });
});