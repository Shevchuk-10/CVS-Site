const accountData = {
    'Личный': { posts: [], projects: [] },
    'Рабочий': { posts: [], projects: [] },
};

let currentAccount = 'Личный';

function selectAccount(element, name) {
    document.querySelectorAll('.account').forEach(el => el.classList.remove('active'));
    element.classList.add('active');
    currentAccount = name;
    renderData();
}

function addPost() {
    const input = document.getElementById('postInput');
    if (input.value.trim()) {
        accountData[currentAccount].posts.push(input.value);
        input.value = '';
        renderData();
    }
}

function addProject() {
    const input = document.getElementById('projectInput');
    if (input.value.trim()) {
        accountData[currentAccount].projects.push(input.value);
        input.value = '';
        renderData();
    }
}

function renderData() {
    const postList = document.getElementById('postList');
    const projectList = document.getElementById('projectList');
    postList.innerHTML = '';
    projectList.innerHTML = '';
    accountData[currentAccount].posts.forEach(post => {
        const li = document.createElement('li');
        li.textContent = post;
        postList.appendChild(li);
    });
    accountData[currentAccount].projects.forEach(project => {
        const li = document.createElement('li');
        li.textContent = project;
        projectList.appendChild(li);
    });
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('hidden');
}

renderData();