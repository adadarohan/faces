const fake_url = fake[Math.floor(Math.random() * fake.length)];
const real_url = real[Math.floor(Math.random() * real.length)];
const eles = ['correct', 'wrong']
const last_ele = eles[Math.floor(Math.random() * eles.length)];

document.getElementById('wrong_img').src = fake_url;
document.getElementById('correct_img').src = real_url;
console.log(last_ele)
document.getElementById(last_ele).classList.add('order-last');
