class Post extends HTMLElement {
  constructor() {
    super();
    this.postBodayClass = 'post-body';

    // Create a shadow root
    const shadow = this.attachShadow({mode: 'open'});    // Sets and returns this.shadowRoot

    // Create (nested) span elements
    const contentWrapper = document.createElement('div');
    contentWrapper.setAttribute('class', 'wrapper');
    contentWrapper.setAttribute('style', `
    overflow: auto;
    `);

    const header = contentWrapper.appendChild(
        document.createElement('div')
    );
    header.setAttribute('class', 'post-header');

    const title = header.appendChild(
        document.createElement('h2')
    );

    title.setAttribute('class','title');
    // Take attribute content and put it inside the info span
    title.textContent = this.getAttribute('title');

    const author = header.appendChild(
        document.createElement('span')
    );
    author.setAttribute('class','author');
    author.setAttribute('style', `
      float: left;
      padding-left: 10px;
      font-weight: bold;
    `);
    // Take attribute content and put it inside the info span
    author.textContent = this.getAttribute('author');

    const date = header.appendChild(
        document.createElement('span')
    );
    date.setAttribute('class','date');
    // Take attribute content and put it inside the info span
    date.textContent = this.getAttribute('date');
    date.setAttribute('style', `
      padding-left: 10px;
      font-style: italic;
    `);


    const body = contentWrapper.appendChild(
        document.createElement('div')
    );
    body.setAttribute('class', this.postBodayClass);
    body.setAttribute('style', `
      padding-left: 20px;
    `);

    const content = body.appendChild(
        document.createElement('div')
    );
    content.setAttribute('class','content');
    content.setAttribute('style', `
    `);

    // Take attribute content and put it inside the info span
    content.innerHTML = this.getAttribute('content');

    contentWrapper.appendChild(body);
    const footer = document.createElement('div')
    footer.setAttribute('class', 'post-footer');
    shadow.appendChild(contentWrapper);
  }

  connectedCallback() {
    console.log('Custom Post element added to page.');
  }

  disconnectedCallback() {
    console.log('Custom Post element removed from page.');
  }

  adoptedCallback() {
    console.log('Custom Post element moved to new page.');
  }

  attributeChangedCallback(name, oldValue, newValue) {
    console.log('Custom Post element attributes changed.');
  }

}

customElements.define('post-item', Post);
