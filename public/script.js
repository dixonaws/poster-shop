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
				console.log("addToCart(" + product.id + ")");

				this.total += product.price;

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
						price: product.price,
						qty: 1
					});

				}

			}, // addToCart()

			removeFromCart: function (item) {
				console.log("removeFromCart(" + item.id + ")");

				item.qty--;

				this.total -= item.price;

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

				// use vue-resouce to query the API
				var path = "https://9dyfqj0359.execute-api.us-east-1.amazonaws.com/api/search/".concat(this.search);
				this.$http.get(path).then(function (response) {
					setTimeout(function () {

						this.loading = false;
						this.lastSearch = this.search;
						if (response.body === null) {
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
