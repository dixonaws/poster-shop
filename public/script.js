var LOAD_NUM = 4;
var watcher;

setTimeout(function () {
	new Vue({
		el: "#app",
		data: {
			total: 0,
			products: [],
			cart: [],
			search: "dog",
			lastSearch: "",
			loading: false,
			results: []

		}, // data()

		created: function () {
			this.onSubmit();
		}, // created()

		updated: function () {
			var sensor = document.querySelector("#product-list-bottom");
			watcher = scrollMonitor.create(sensor);
			watcher.enterViewport(this.appendResults);
		}, // updated()

		beforeUpdate: function () {
			if (watcher) {
				watcher.destroy();
				watcher = null;
			}

		}, // beforeUpdate()

		methods: {
			addToCart: function (product) {
				console.log("addToCart: adding product " + product.id + " to cart");

				console.log("summing price is " + product.price);
				this.total += parseFloat(product.price);

				var found = false;
				for (var i = 0; i < this.cart.length; i++) {
					if (this.cart[i].id == product.id) {
						this.cart[i].qty++;
						found = true;
					}
				}

				if (!found) {
					this.cart.push({
						id: product.id,
						title: product.title,
						price: parseFloat(product.price),
						qty: 1
					});

				}

			}, // addToCart()

			removeFromCart: function (item) {
				console.log("removeFromCart(" + item.id + ")");

				item.qty--;

				this.total -= parseFloat(item.price);

				if (item.qty <= 0) {
					var i = this.cart.indexOf(item);
					this.cart.splice(i, 1);
				}


			}, // removeFromCart()
			onSubmit: function () {
				console.log("search term: " + this.search);
				this.products = [];
				this.results = [];
				this.loading = true;

				// use vue-resource to query the API
				var str_url = "https://9dyfqj0359.execute-api.us-east-1.amazonaws.com/api/search/";
				var path = str_url.concat(this.search);

				console.log("Using path: " + path);


				this.$http.get(path).then(function (response) {
					setTimeout(function () {
						this.loading = false;
						this.lastSearch = this.search;

						if (response.body === null || response.body.length==undefined) {
							console.log("Nothing found!");
							this.results = [];
						} else {
							this.results = response.body;
							this.appendResults();
						}

					}.bind(this), 300);

				});

			}, // onSubmit()


			appendResults: function () {
				if (this.products.length < this.results.length) {
					var toAppend = this.results.slice(
						this.products.length,
						LOAD_NUM + this.products.length
					);
					this.products = this.products.concat(toAppend);
				}
			} // appendResults()

		}, // methods

		filters: {
			currency: function (value) {
				var formatter = new Intl.NumberFormat("en-US", {
					style: "currency",
					currency: "USD",
					minimumFractionDigits: 2
				});
				return (formatter.format(value));
			}
		}
	});

}, 1000);
