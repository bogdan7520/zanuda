var intervalfirst = setTimeout(funcintervalfirst, 1);
  function funcintervalfirst() {
  var for_one_plus = 0;
  var some_num = 1;
  all_func(for_one_plus, some_num)
  }
function all_func(for_one_plus, some_num) {
    document.getElementById('button_right_id').addEventListener('click', for_right)

    function for_right(){
    func_click_right_button(for_one_plus += 1, some_num)
    }

    function func_click_right_button(for_one_plus, some_num) {
    var for_one_plus = String(for_one_plus)


    f = some_num
    var click_var = 'right'
    //var some_var = ('photo_'+for_one_plus)
    //var for_one_minus = String(Number(for_one_plus) - 1)
    //var some_var_two = ('photo_'+for_one_minus)

    for_left = (-80*Number(for_one_plus))
    for_count(click_var, for_left, for_one_plus)
    //document.getElementById(some_var).style.cssText = 'height: 70vh; right: 0vw; top: 0vh;';
    //document.getElementById(some_var_two).style.cssText = 'height: 0vh; right: 0vw; top: 0vh;';
    //document.getElementById('photo_'+String(Number(for_one_plus+2))).style.cssText = 'height: 70vh; right: 0vw; top: 0vh;';
    //document.getElementById('title_detail').style.cssText = 'color: red';

    //document.getElementById('div_for_photos_id').setAttribute('class', 'div_for_photos_2')
    //document.getElementById('div_for_photos_id').style.left = for_left + 'vw'
    }

    document.getElementById('button_left_id').addEventListener('click', for_left);

    function for_left(){
    func_click_left_button(for_one_plus -= 1, some_num)
    }

    function func_click_left_button(for_one_plus, some_num) {
    var for_one_plus = String(for_one_plus)
    var f = some_num

    var click_var = 'left'
    //var some_var = ('photo_'+for_one_plus)
    //var for_one_minus = String(Number(for_one_plus) - 1)
    //var some_var_two = ('photo_'+for_one_minus)

    for_left = (-80*Number(for_one_plus))
    for_count(click_var, for_left, for_one_plus)

    //var some_var = ('photo_'+for_one_plus)
    //var for_one_minus = String(Number(for_one_plus) + 1)
    //var some_var_two = ('photo_'+for_one_minus)
   // console.log(some_var_two)
   // console.log(some_var)

    //document.getElementById(some_var).style.cssText = 'height: 70vh; right: 0vw; top: 0vh;';
    //document.getElementById(some_var_two).style.cssText = 'height: 0vh; right: 0vw; top: 0vh;';
    //document.getElementById('photo_'+String(Number(for_one_plus+2))).style.cssText = 'height: 0vh; right: 0vw; top: 0vh;';
    //document.getElementById('title_detail').style.cssText = 'color: #333';

    //document.getElementById('div_for_photos_id').setAttribute('class', 'div_for_photos')
    }

    function for_count(click_var, for_left, for_one_plus) {

        var count_img_var = Number(document.getElementById('div_for_photos_id').getElementsByTagName('img').length)



        if (click_var == 'right') {
        if (Number(for_one_plus) <= (count_img_var - 1)){
        document.getElementById('div_for_photos_id').style.left = for_left + 'vw'
        document.getElementById('button_left_id').style.cssText = 'border-top: 15px solid #333;border-left: 15px solid #333;width: 25px;height: 25px;'
        }
        else if (for_one_plus == count_img_var) {
        //var for_one_plus = (for_one_plus - 7);
        //var for_one_plus = (for_one_plus+1)
        //var some_num = 1;
        //for_left = (-35*Number(for_one_plus))
        //document.getElementById('div_for_photos_id').style.left = for_left + 'vw'
        document.getElementById('button_right_id').style.cssText = 'height: 0vh; width: 0vw; border: 0px solid black;'
        //document.getElementById('button_left_id').style.cssText = 'top: 45vh;'
        //func_click_left_button(for_one_plus, some_num)

         }
        }

            else if (click_var == 'left') {
            if (for_one_plus >= 0){
            for_one_plus = (for_one_plus - 1)
            for_left = (-80*Number(for_one_plus))
            for_right = (for_left - 80)
            document.getElementById('div_for_photos_id').style.left = for_right + 'vw'
            document.getElementById('button_right_id').style.cssText = 'border-top: 15px solid #333;border-right: 15px solid #333;width: 25px;height: 25px;'
            }

            else if (for_one_plus < 0) {
            //document.getElementById('div_for_photos_id').style.left = for_left + 'vw'
            document.getElementById('button_left_id').style.cssText = 'height: 0px; width: 0px; border: 0px solid black;'

            //func_click_left_button(for_one_plus, some_num)

             }
            }

      }
    }