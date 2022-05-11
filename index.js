const real_url = real[Math.floor(Math.random() * real.length)];
const eles = ['correct', 'wrong']
const last_ele = eles[Math.floor(Math.random() * eles.length)];

document.getElementById('wrong_img').src = 'https://thispersondoesnotexist.com/image';
document.getElementById('correct_img').src = real_url;
document.getElementById('correct_img').onload = () => {
    document.getElementById('pics').style.display = 'flex';
}

console.log(last_ele)
document.getElementById(last_ele).classList.add('order-last');
