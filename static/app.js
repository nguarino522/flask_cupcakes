function generateCupcakeHTML(cupcake) {

    return `
        <div class="col-3">
        <div class="card container alert alert-info text-center" id="cupcake" data-cupcake-id=${cupcake.id}>
            <img src="${cupcake.image}" class="card-img-top cupcake-img">
            <div class="card-body">
            <h4 class="card-title">${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}</h4>
            <button type="submit" class="btn btn-danger delete-button">Delete Cupcake!</button>
            </div>
        </div>
        </div>
        `;
}

async function populateInitialCupcakes() {
    let resp = await axios.get("/api/cupcakes")

    for (let cupcake of resp.data.cupcakes) {
        let newCupcake = $(generateCupcakeHTML(cupcake));
        $("#currentcupcakes").append(newCupcake);
    }
}

populateInitialCupcakes();

$("#new-cupcake-form").on("submit", async function (evt) {
    evt.preventDefault();

    let flavor = $("#flavor").val();
    let rating = $("#rating").val();
    let size = $("#size").val();
    let image = $("#image").val();
    let newCupcakeResponse = await axios.post(`/api/cupcakes`, {flavor, rating, size, image: image});
    let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
    $("#currentcupcakes").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");
});



document.getElementById("currentcupcakes").addEventListener("click", async function (e) {
    e.preventDefault();

    let elementToDelete = e.target.parentElement.parentElement.parentElement;
    cupcakeId = e.target.parentElement.parentElement.dataset.cupcakeId
    await axios.delete(`/api/cupcakes/${cupcakeId}`);
    elementToDelete.remove();
});