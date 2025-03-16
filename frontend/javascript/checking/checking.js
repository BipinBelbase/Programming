function resolveAfter2Seconds() {
    return new Promise((resolve, reject) =>{
        setTimeout(() => {
            resolve("resolved");

        },3000);
    });
}

async function checkingAsync() {
    console.log("calling....");
    const result = await resolveAfter2Seconds();
    console.log(result);

}
checkingAsync();