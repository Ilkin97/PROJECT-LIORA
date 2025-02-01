document.addEventListener('DOMContentLoaded', function () {
    const priceInput = document.querySelector('input[name="price"]');
    const discountInput = document.querySelector('input[name="discount_percentage"]');
    const discountPriceInput = document.querySelector('input[name="discount_price"]');

    function updateDiscountPrice() {
        const price = parseFloat(priceInput.value);
        const discountPercentage = parseFloat(discountInput.value);

        if (!isNaN(price) && !isNaN(discountPercentage)) {
            const discountPrice = price - (price * discountPercentage / 100);
            discountPriceInput.value = discountPrice.toFixed(2);
        } else {
            discountPriceInput.value = '';
        }
    }

    if (priceInput && discountInput && discountPriceInput) {
        priceInput.addEventListener('input', updateDiscountPrice);
        discountInput.addEventListener('input', updateDiscountPrice);
    }
});
