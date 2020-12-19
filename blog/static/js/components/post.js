class Post extends HTMLElement {
  constructor() {
    super();

    // Create a shadow root
    const shadow = this.attachShadow({mode: 'open'});    // Sets and returns this.shadowRoot
    let style = null;

    // Create (nested) span elements
    const wrapper = document.createElement('span');
    wrapper.setAttribute('class', 'wrapper');

    const title = wrapper.appendChild(
        document.createElement('span')
    );
    title.setAttribute('class','title');
    // Take attribute content and put it inside the info span
    title.textContent = this.getAttribute('title');
    style = title.appendChild(
        document.createElement('style')
    );
    style.textContent = `
    color: red;
    `;

    // Add the collapse button
    const btn = wrapper.appendChild(
        document.createElement('span')
    );
    btn.setAttribute('class', 'post-collapse');
    btn.setAttribute('tabindex', 0);
    btn.innerHTML = '<ion-icon name="chevron-up-outline"></ion-icon>';
    style = btn.appendChild(
        document.createElement('style')
    );
    style.textContent = `color: blue;`;

    const date = wrapper.appendChild(
        document.createElement('span')
    );
    date.setAttribute('class','date');
    // Take attribute content and put it inside the info span
    date.textContent = this.getAttribute('date');
    style = date.appendChild(
        document.createElement('style')
    );
    style.textContent = `color: orange;`;

    const author = wrapper.appendChild(
        document.createElement('span')
    );
    author.setAttribute('class','author');
    // Take attribute content and put it inside the info span
    author.textContent = this.getAttribute('author');
    style = author.appendChild(
        document.createElement('style')
    );

    style.textContent = `color: pink;`;

    const content = wrapper.appendChild(
        document.createElement('span')
    );
    content.setAttribute('class','content');
    // Take attribute content and put it inside the info span
    content.innerHTML = this.getAttribute('content');
    style = content.appendChild(
        document.createElement('style')
    );
    style.textContent = `color: black;`;

    style = document.createElement('style');
    style.textContent = `color: green`;
    shadow.appendChild(style);
    shadow.appendChild(wrapper);

    console.log(shadow);
  }
}

customElements.define('post-item', Post);
