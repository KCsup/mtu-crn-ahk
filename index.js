const FORM_ID = "test-form";

document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById(FORM_ID).addEventListener("submit", function(e) {
        for(let i = 0; i < this.elements.length; i++) {
            let value = this.elements[i].value;
            if(value) console.log(value);
        }
        e.preventDefault();
    });
});

