// let helloWorld = "hello World";
// console.log(helloWorld);
// helloWorld = "hello Kaspars";
// console.log(helloWorld);
// helloWorld = 11;
// console.log(helloWorld);
// helloWorld = 1.5;
// console.log(helloWorld);

// let isDrunk = false;
// console.log(isDrunk);

// function myFunction(p1, p2) {
//     return p1 * p2;
// }

// function drinkBeer(yes) {
//     if (yes === true) {
//         isDrunk = true;

//     }

// }
// drinkBeer(true);
// console.log(isDrunk);




//
// let carBrand = ["VOLVO", "Toyota", "Nissan"];
// for (let i = 0; i < carBrand.length; i++) {
//     console.log(carBrand[i])
//     console.log(i)
// }
// let i = 0
// while (i < carBrand.length) {
//     console.log(carBrand[i])
//     console.log(i)
//     i++;
// }

function enlargeImg() {
    const picture = document.querySelector('.index-pictures');
    picture.addEventListener('mouseover', function(e) {
        const target = e.target;
        if (target.classList.contains('picture')) {
            target.style.transform = "scale(1.2)";
            target.style.transition = "transform 0.3s ease";
        }
    });
}

function shrinkImg() {
    const picture = document.querySelector('.index-pictures');
    picture.addEventListener('mouseout', function(e) {
        const target = e.target;
        if (target.classList.contains('picture')) {
            target.style.transform = "scale(1)";
            target.style.transition = "transform 0.3s ease";
        }
    });
}



function keyDownEvent() {
    document.getElementById("input1");
    alert("pressed a key");
}



