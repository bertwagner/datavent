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
                
                numeric_price = Number(product.dataset.price.replace(/[^0-9.-]+/g,""));

                item_total += numeric_price;
                
                cart_ui_list.innerHTML = cart_ui_list.innerHTML + `<li class="list-group-item d-flex justify-content-between lh-sm">
                <div` + (numeric_price < 0 ? " class='text-success'" : "") + `>
                  <h6 class="my-0">${product.dataset.name}</h6>
                  <small class="text-body-secondary">${product.dataset.description}</small>
                </div>
                <span class="text-body-secondary` + (numeric_price < 0 ? " text-success" : "") + `">${product.dataset.price == "$0.00" ? 'FREE' : product.dataset.price}</span>
              </li>`
            }
        });


        // display total
        // never allow negative totals (due to coupons applied without addons)
        if (item_total < 0) {
            item_total = 0;
        }
        cart_ui_list.innerHTML = cart_ui_list.innerHTML + `<li class="list-group-item d-flex justify-content-between">
            <span>Total (USD)</span>
            <strong>${USDollar.format(item_total)}</strong>
        </li>`
        
        document.querySelector("#cart-count").innerHTML = shopping_cart.length;
    };

    function check_coupon(code) {
        fetch('/coupon', {
            method: 'POST',
            body: JSON.stringify({coupon: encodeURIComponent(code)}),
            headers: {
                'Content-Type': 'application/json'
            },
            referrer: 'no-referrer'
        }).then(function (response) {

            // The API call was successful!
            if (response.ok) {
                return response.json();
            }

            // There was an error
            return Promise.reject(response);

        }).then(function (data) {
            if (data['is_valid'] == true) {
                hidden_products = document.querySelector("#hidden-products");
                hidden_products.innerHTML = hidden_products.innerHTML + `<input type="hidden" class="product" id="${data['id']}" checked="checked" data-price="${data['price']}" data-description="${data['description']}" data-name="${data['name']}"></input>`;
            }
            update_cart();
        }).catch(function (err) {
            // There was an error
            console.warn('Error: ', err);
        });

        
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
            check_coupon(document.querySelector("#promo-code").value);
            // clear value
            document.querySelector("#promo-code").value = '';
        };
    });

    update_cart();

})();