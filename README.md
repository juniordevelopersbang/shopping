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

