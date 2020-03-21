첫 과제
=======

bootstrap이라는 좋은 프레임워크를 이용해서 큰 틀을 쉽게 만들 수 있었다.
하지만 내가 원하는대로 세세하게 바꿀려고하니 몇가지 문제가 있었다.

1. 사진의 크기가 안맞는다
------------------------
> 수업시간에 배운 .container를 이용해 가운데 정렬을 했지만 내가 생각한 거와 달리 정렬은 됐지만 사진의 크기는 변하지않았다.
>>그래서 직접 웹페이지에서 F12를 눌러서 width을 확인하고 수정했다.

  
    .macbook{
    width: 690px;
    height: auto;
    padding-bottom: 2rem;
    }

2. 상품을 설명하는 글에 이름은 크게 가격은 작게 설정하고 싶었지만     P태크에서 고민했다.
  > display를 inline으로도 바꿔보고 text-aligin을 center, left, right를 다 해보았지만 원하는대로 되지않았다.
  고질적인 문제는 같은 p태크안에 이름과 가격을 같이 쓰면 css가 같이 적용되고 다른 p태그에 쓰면 사이에 공간이 생긴다는 것이었다.
  >>의외로 해결방법은 아주 간단했다. 바로 span태그를 이용하는 것이다. span태그를 사용하니 css도 따로 적용하고 원하던대로 옆으로 왔다.
  
      <span class="title">
        맥북을 팝니다.
      </span>
      <span class="price">
        가격: 3000000만원/1개
      </span>
      
 3. 마지막 주문하기 버튼이 가운데로 오지 않았다.
 > 수업시간에 배운 .container를 사용하면 당연히 가운데로 올 줄 알았던 버튼이 왼쪽에 위치한 것이다. 
 그래서 구글링한 결과 "text-center"라는 클래스로 구성된 div클래스로 가두었더니 해결되었다.

    <div class="text-center">
        <button type="button" class="btn btn-primary">주문하기</button>
      </div>

2주차 과제
==========

이번 과제는 javascript와 jQuery를 이용하여 1주차 때 만들었던 쇼핑몰 페이지에 정보를 입력할 때 알림이 뜨게 만들었다.

수업시간에 푼 퀴즈와 비슷해서 간단하게 해결할 수 있었다.

1. 각각의 input 태그에 id를 부여했다.

     <input
          id="name"
    <input
          id="address"
    select id="count"

    <input
          id="number"

2. order()라는 function을 만들었다.
     
        function order() {
          let name = $("#name").val();
          let count = document.getElementById("count");
          let address = $("#address").val();
          let number = $("#number").val();

          if (name === "") {
            alert("이름을 입력하세요!");
          } else if (count.options[count.selectedIndex].value === "0") {
            alert("수량을 선택하세요!");
          } else if (address === "") {
            alert("주소를 입력하세요!");
          } else if (number === "") {
            alert("전화번호를 입력하세요!");
          }else{
            alert("주문이 완료되었습니다.")
          }
        }

각각의 변수에 val()이라는 함수를 이용해서 입력값을 가져와서 if문에 사용했다. 
count변수는 val()로 입력값을 선택하는 것이 안되서 구글에 검색한결과 getElementById라는 함수를 이용해 입력값을 가져왔다.
       
       <select id="count" class="custom-select" id="inputGroupSelect01">
          <option value="0">---수량을 선택하세요---</option>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
        </select>
     
        count.options[count.selectedIndex].value === "0"

valye = "0"인 부분이 원래 selected였는데 if문을 사용해주기 위해 value = "0"이라고 바꿨는데 문제없이 잘 해결되었다.

