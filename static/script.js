// script.js

async function fetchProducts() {
    const response = await fetch('/api/products'); // Fetch data from the Flask backend
    const products = await response.json();
    displayProducts(products);
}

function displayProducts(products) {
    const productList = document.getElementById('productList');
    productList.innerHTML = '';

    products.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.classList.add('product');
        productDiv.innerHTML = `
            <h2>${product.name}</h2>
            <img src="${product.image}" alt="${product.name}" style="width:200px;">
            <p>Price: ₹${product.discount_price}</p>
            <p>Rating: ${product.ratings} ⭐</p>
            <a href="${product.link}" target="_blank">Buy Now</a>
        `;
        productList.appendChild(productDiv);
    });
}

function filterProducts() {
    const query = document.getElementById('searchBar').value.toLowerCase();
    const productDivs = document.querySelectorAll('.product');
    productDivs.forEach(productDiv => {
        const productName = productDiv.querySelector('h2').innerText.toLowerCase();
        if (productName.includes(query)) {
            productDiv.style.display = 'block';
        } else {
            productDiv.style.display = 'none';
        }
    });
}

// Fetch products when the page is loaded
fetchProducts();
