;(function () {
    ////
    // variables
    ////
    let shopping_cart = [];
    let coupons = [];

    ////
    // methods
    ////

    function update_cart() {
        let products = document.querySelectorAll(".product");

        let shopping_cart = []
        cart_ui_list = document.querySelector("#cart-list");

        let USDollar = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
        });

        let item_total = 0;

        // clear the cart
        cart_ui_list.innerHTML = ''
        
        products.forEach(function(product,index) {
            if (product.checked){
                shopping_cart.push({"id": product.id, "name": product.dataset.name, "description": product.dataset.description, "price": product.dataset.price});
                item_total += Number(product.dataset.price.replace(/[^0-9.-]+/g,""));
                cart_ui_list.innerHTML = cart_ui_list.innerHTML + `<li class="list-group-item d-flex justify-content-between lh-sm">
                <div>
                  <h6 class="my-0">${product.dataset.name}</h6>
                  <small class="text-body-secondary">${product.dataset.description}</small>
                </div>
                <span class="text-body-secondary">${product.dataset.price == "$0.00" ? 'FREE' : product.dataset.price}</span>
              </li>`
            }
        });

        // do coupon math
        // cart_ui_list.innerHTML = cart_ui_list.innerHTML + `<li class="list-group-item d-flex justify-content-between bg-body-tertiary">
        //   <div class="text-success">
        //     <h6 class="my-0">Promo code</h6>
        //     <small>FREEVOLUNTEERLUNCH</small>
        //   </div>
        //   <span class="text-success">−$16</span>
        // </li>`

        // display total
        cart_ui_list.innerHTML = cart_ui_list.innerHTML + `<li class="list-group-item d-flex justify-content-between">
            <span>Total (USD)</span>
            <strong>${USDollar.format(item_total)}</strong>
        </li>`
        
        document.querySelector("#cart-count").innerHTML = shopping_cart.length;
    };

    function check_coupon() {
        // TODO: use fetch() to confirm coupon code
        
        return 
    };


    ////
    // inits
    ////

    document.addEventListener('click', function (event) {
        if (event.target.classList.contains("product")) {
            update_cart();
        };

        if (event.target.id == "coupon-redeem") {
            event.preventDefault();
            check_coupon();
            update_cart();
        };
    });

    update_cart();

})();