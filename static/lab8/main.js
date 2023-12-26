function fillCourseList(){
    fetch('/lab8/api/courses/')
    .then(function (data) {
        return data.json();
    })
    .then(function (courses){
        let tbody = document.getElementById('course-list');
        tbody.innerHTML = '';
        for(let i = 0; i<courses.length; i++) {
            tr = document.createElement('td');

            let tdName = document.createElement('td');
            tdName.innerText = courses[i].name;

            let tdVideos = document.createElement('td');
            tdVideos.innerText = courses[i].videos;

            let tdPrice = document.createElement('td');
            tdPrice.innerText = courses[i].price || 'бесплатно';

            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';

            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';
            delButton.onclick = function(){
                deleteCourse(i);
            };

            let tdActions = document.createElement('td');
            tdActions.append(editButton);
            tdActions.append(delButton);

            tr.append(tdName);
            tr.append(tdVideos);

            tbody.append(tr);
        }
    })
}

function fillCourseList(){
    fetch('/lab8/api/courses/')
    .then (function (data) {
        return data.json();
    })
    .then(function (courses) {

    })
}

function deleteCourse(num) {
    if(! confirm('Вы точно хотите удалить курс?'))
        return;

    fetch(`/lab8/api/courses/${num}`, {method: 'DELETE'})
    .then(function () {
        fillCourseList();
    });
}

function showModal(){
    document.querySelector('div.modal').computedStyleMap.display = 'block'
}

function hideModal(){
    document.querySelector('div.modal').computedStyleMap.display = 'none'
}

function cancel(){
    hideModal();
}

function addCourse(){
    document.getElementById('num').value = '';
    document.getElementById('name').value = '';
    document.getElementById('videos').value = '';
    document.getElementById('price').value = '';
    showModal();
}

function sendCourse(){
    const course = {
        name: document.getElementById('name').value,
        videos: document.getElementById('videos').value,
        price: document.getElementById('price').value,
    }
    const url = `/lab8/api/courses/`;
    const method = 'POST';
    fetch (url, {
        method: method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(course)
    })
    .then(function(){
        fillCourseList();
        hideModal();
    });
}