// main.js — vanilla JS AJAX for HTML partials

function handleEdit(e) {
    const id = e.currentTarget.dataset.id;
    fetch(window.location.pathname + id + '/json/')
        .then(r => r.json())
        .then(data => {
            qs('#id_name').value = data.name;
            qs('#id_email').value = data.email;
            qs('#id_age').value = data.age;
            qs('#id_notes').value = data.notes;
            qs('#member-id').value = data.id;
            qs('#submit-btn').textContent = 'Update';
            qs('#cancel-btn').style.display = 'inline-block';
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
}

function handleDelete(e) {
    const id = e.currentTarget.dataset.id;
    if (!confirm('Delete this member?')) return;

    fetch(window.location.pathname + id + '/delete/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
    })
        .then(resp => resp.text())
        .then(html => {
            qs('#members-list').innerHTML = html;
            attachRowHandlers();
        });
}

document.addEventListener('DOMContentLoaded', function () {
    attachRowHandlers();

    const form = qs('#member-form');
    form.addEventListener('submit', function (ev) {
        ev.preventDefault();

        const id = qs('#member-id').value;
        const url = id
            ? (window.location.pathname + id + '/update/')
            : (window.location.pathname + 'create/');
        const formData = new FormData(form);

        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken,
            },
            body: formData,
        })
            .then(resp => {
                if (resp.ok) return resp.text();
                return resp.json().then(err => { throw err; });
            })
            .then(html => {
                qs('#members-list').innerHTML = html;
                attachRowHandlers();
                resetForm();
            })
            .catch(err => {
                if (err.errors) {
                    showErrors(err.errors);
                } else {
                    showErrors({ 'error': ['An unknown error occurred'] });
                }
            });
    });

    qs('#cancel-btn').addEventListener('click', function () {
        resetForm();
    });
});
