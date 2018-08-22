function fadeOut(){
TweenMax.to("#myBtn", 1, {

  y: -400,
  opacity: 0

});

TweenMax.to(".screen", 2, {

  y: -400,
  opacity: 0,
  ease: Power2.easeInOut,
  delay: 2.6

});

TweenMax.from(".overlay", 2, {

  ease: Power2.easeInOut

});

TweenMax.to(".overlay", 2, {

  top: "-110%",
  ease: Expo.easeInOut,
  delay: 2.6

});

TweenMax.to(".overlay-2", 2 , {

  top: "-110%",
  ease: Expo.easeInOut,
  delay: 3.2

});

TweenMax.from(".main-page", 2, {

  opacity: 0,
  ease: Power2.easeInOut,
  delay: 3.2


});

TweenMax.to(".main-page", 2, {

  opacity: 1,
  y: -300,
  ease: Power2.easeInOut,
  delay: 3.2


});

}
