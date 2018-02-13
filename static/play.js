
$(function() {
    $('.selectpicker').selectpicker({
        style: 'btn-primary',
        size: 6
    });
})



function toggleChevron(e) {
	$(e.target)
		.prev('.panel-heading')
		.find("i.indicator")
		.toggleClass('fa-caret-down fa-caret-right');
	}
$('#accordion').on('hidden.bs.collapse', toggleChevron);
$('#accordion').on('shown.bs.collapse', toggleChevron);



function save(){
            var checkboxAll = document.getElementById('checkAll');
            sessionStorage.setItem('checkAll', checkboxAll.checked);

            var checkboxSection = document.getElementById('filial');
            sessionStorage.setItem('filial', checkboxSection.checked);

            var checkboxSection = document.getElementById('CodeSection');
            sessionStorage.setItem('CodeSection', checkboxSection.checked);

            var checkboxSection = document.getElementById('NameProduct');
            sessionStorage.setItem('NameProduct', checkboxSection.checked);


            var checkboxSection = document.getElementById('code-of-section');
            sessionStorage.setItem('code-of-section', checkboxSection.checked);

            var checkboxProduct = document.getElementById('code-of-product');
            sessionStorage.setItem('code-of-product', checkboxProduct.checked);

            var checkboxFilial = document.getElementById('type-of-filial');
            sessionStorage.setItem('type-of-filial', checkboxFilial.checked);

            var checkbox1c = document.getElementById('code-of-1c');
            sessionStorage.setItem('code-of-1c', checkbox1c.checked);

            var checkboxPieces = document.getElementById('pieces-per-pack');
            sessionStorage.setItem('pieces-per-pack', checkboxPieces.checked);

            var checkboxMeasure = document.getElementById('measure-chk');
            sessionStorage.setItem('measure-chk', checkboxMeasure.checked);

            var checkboxType = document.getElementById('type');
            sessionStorage.setItem('type', checkboxType.checked);

            var checkboxBuyer = document.getElementById('buyer');
            sessionStorage.setItem('buyer', checkboxBuyer.checked);

            var checkboxCountry = document.getElementById('country');
            sessionStorage.setItem('country', checkboxCountry.checked);

            var checkboxSegment = document.getElementById('price-segment');
            sessionStorage.setItem('price-segment', checkboxSegment.checked);

            var checkboxLevel = document.getElementById('level-1');
            sessionStorage.setItem('level-1', checkboxLevel.checked);

            var checkboxLevel2 = document.getElementById('level-2');
            sessionStorage.setItem('level-2', checkboxLevel2.checked);

            var checkboxLevel3 = document.getElementById('level-3');
            sessionStorage.setItem('level-3', checkboxLevel3.checked);

            var checkboxLevel4 = document.getElementById('level-4');
            sessionStorage.setItem('level-4', checkboxLevel4.checked);

            // var checkboxProductGroup = document.getElementById('product-group');
            // sessionStorage.setItem('product-group', checkboxProductGroup.checked);

            var checkboxMarketer = document.getElementById('marketer');
            sessionStorage.setItem('marketer', checkboxMarketer.checked);

            var checkboxDescription = document.getElementById('description');
            sessionStorage.setItem('description', checkboxDescription.checked);

            var checkboxCash = document.getElementById('cash-price');
            sessionStorage.setItem('cash-price', checkboxCash.checked);

            var checkboxDataPrice = document.getElementById('data-of-price');
            sessionStorage.setItem('data-of-price', checkboxDataPrice.checked);

            var checkboxBalanceData = document.getElementById('balance-data');
            sessionStorage.setItem('balance-data', checkboxBalanceData.checked);

            var checkboxWeight = document.getElementById('weight');
            sessionStorage.setItem('weight', checkboxWeight.checked);

            var checkboxVolume = document.getElementById('volume');
            sessionStorage.setItem('volume', checkboxVolume.checked);
            //
            // var checkboxProductPhoto = document.getElementById('product-photo');
            // sessionStorage.setItem('product-photo', checkboxProductPhoto.checked);
            $("#loading").show();
            $("#info-table").hide();

            console.log("save")
}

function load() {

            var checkedAll = JSON.parse(sessionStorage.getItem('checkAll'));
            document.getElementById("checkAll").checked = checkedAll;

            var checkedFilial = JSON.parse(sessionStorage.getItem('filial'));
            document.getElementById("filial").checked = checkedFilial;

            var checkedCodeSection = JSON.parse(sessionStorage.getItem('CodeSection'));
            document.getElementById("CodeSection").checked = checkedCodeSection;

            var checkedNameProduct = JSON.parse(sessionStorage.getItem('NameProduct'));
            document.getElementById("NameProduct").checked = checkedNameProduct;


            var checkedSection = JSON.parse(sessionStorage.getItem('code-of-section'));
            document.getElementById("code-of-section").checked = checkedSection;

            var checkedProduct = JSON.parse(sessionStorage.getItem('code-of-product'));
            document.getElementById("code-of-product").checked = checkedProduct;

            var checkedFilial = JSON.parse(sessionStorage.getItem('type-of-filial'));
            document.getElementById("type-of-filial").checked = checkedFilial;

            var checked1c = JSON.parse(sessionStorage.getItem('code-of-1c'));
            document.getElementById("code-of-1c").checked = checked1c;

            var checkedPieces = JSON.parse(sessionStorage.getItem('pieces-per-pack'));
            document.getElementById("pieces-per-pack").checked = checkedPieces;

            var checkedMeasure = JSON.parse(sessionStorage.getItem('measure-chk'));
            document.getElementById("measure-chk").checked = checkedMeasure;

            var checkedType = JSON.parse(sessionStorage.getItem('type'));
            document.getElementById("type").checked = checkedType;

            var checkedBuyer = JSON.parse(sessionStorage.getItem('buyer'));
            document.getElementById("buyer").checked = checkedBuyer;

            var checkedCountry = JSON.parse(sessionStorage.getItem('country'));
            document.getElementById("country").checked = checkedCountry;

            var checkedSegment = JSON.parse(sessionStorage.getItem('price-segment'));
            document.getElementById("price-segment").checked = checkedSegment;

            var checkedLevel = JSON.parse(sessionStorage.getItem('level-1'));
            document.getElementById("level-1").checked = checkedLevel;

            var checkedLevel2 = JSON.parse(sessionStorage.getItem('level-2'));
            document.getElementById("level-2").checked = checkedLevel2;

            var checkedLevel3 = JSON.parse(sessionStorage.getItem('level-3'));
            document.getElementById("level-3").checked = checkedLevel3;

            var checkedLevel4 = JSON.parse(sessionStorage.getItem('level-4'));
            document.getElementById("level-4").checked = checkedLevel4;

            // var checkedProductGroup = JSON.parse(sessionStorage.getItem('product-group'));
            // document.getElementById("product-group").checked = checkedProductGroup;

            var checkedMarketer = JSON.parse(sessionStorage.getItem('marketer'));
            document.getElementById("marketer").checked = checkedMarketer;

            var checkedDescription = JSON.parse(sessionStorage.getItem('description'));
            document.getElementById("description").checked = checkedDescription;

            var checkedCash = JSON.parse(sessionStorage.getItem('cash-price'));
            document.getElementById("cash-price").checked = checkedCash;

            var checkedDataPrice = JSON.parse(sessionStorage.getItem('data-of-price'));
            document.getElementById("data-of-price").checked = checkedDataPrice;

            var checkedBalanceData = JSON.parse(sessionStorage.getItem('balance-data'));
            document.getElementById("balance-data").checked = checkedBalanceData;

            var checkedWeight = JSON.parse(sessionStorage.getItem('weight'));
            document.getElementById("weight").checked = checkedWeight;

            var checkedVolume = JSON.parse(sessionStorage.getItem('volume'));
            document.getElementById("volume").checked = checkedVolume;

            // var checkedProductPhoto = JSON.parse(sessionStorage.getItem('product-photo'));
            // document.getElementById("product-photo").checked = checkedProductPhoto;

            console.log("load")
}


function wis(){
    location.reload();
    sessionStorage.clear()

}


 $('input[id="msg"]').keypress(function(e) {
                    if(e.which == 13) {
                        jQuery(this).blur();
                        jQuery('#search_button').focus().click();
                    }
                 });


 $('input[id="password"]').keypress(function(e) {
                    if(e.which == 13) {
                        jQuery(this).blur();
                        jQuery('#login').focus().click();
                    }
                 });



