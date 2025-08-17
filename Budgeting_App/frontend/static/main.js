class CustomSelect {
    constructor(originalSelectElement) {
        this.originalSelect = originalSelectElement;;
        this.customSelect = document.createElement("div");
        this.customSelect.classList.add("select");

        this.originalSelect.querySelectorAll("option").forEach(optionElement => {
            const itemElement = document.createElement("div");
            
            itemElement.classList.add("select_item");
            itemElement.textContent = optionElement.textContent;
            this.customSelect.appendChild(itemElement);

            itemElement.addEventListener("click", () => {
                if (itemElement.classList.contains("select_item--selected")) {
                    this._deselect(itemElement);
                } else {
                    this._select(itemElement);
                }
            });
        });

        this.originalSelect.insertAdjacentElement("afterend", this.customSelect);
    }

    _select(itemElement) {
        const index = Array.from(this.customSelect.children).indexOf(itemElement);
        this.originalSelect.querySelectorAll("option")[index].selected = true;
        itemElement.classList.add("select_item--selected");
    }

    _deselect(itemElement) {
        const index = Array.from(this.customSelect.children).indexOf(itemElement);

        this.originalSelect.querySelectorAll("option")[index].selected = false;
        itemElement.classList.remove("select_item--selected");

    }
}

document.querySelectorAll(".custom-select").forEach(selectElement => {
    new CustomSelect(selectElement);
});
