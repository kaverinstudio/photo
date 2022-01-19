"use strict";

// Сайдбар на мобильных устройствах
var sidebarToggleBtn = document.querySelector('.menu-icon-wrapper');
var menuIcon = document.querySelector('.menu-icon');
var sidebar = document.querySelector('.sidebar');

sidebarToggleBtn.onclick = function () {
  menuIcon.classList.toggle('menu-icon-active');
  sidebar.classList.toggle('sidebar--mobile-activ');
}; // Фиксированный хедер


$(function () {
  var header = $('header');
  var hederHeight = header.height(); // вычисляем высоту шапки

  $(window).scroll(function () {
    if ($(this).scrollTop() > 1) {
      header.addClass('header_fixed');
      $('body').css({
        'paddingTop': hederHeight + 'px' // делаем отступ у body, равный высоте шапки

      });
    } else {
      header.removeClass('header_fixed');
      $('body').css({
        'paddingTop': 0 // удаляю отступ у body, равный высоте шапки

      });
    }
  });
}); // Модальное окно входа в личный кабинет

$('.user-link').on('click', function () {
  $('#modal-login').modal('show');
}); // блокируем поле ввода адреса если оно не требуется и считаем полную стоимость заказа

$('#validationCustom04').change(function () {
  if ($(this).val() == 'Забрать из студии самостоятельно') {
    $('#validationCustom03').prop('disabled', true);
    var price_order = $('#price_order').html();
    $('#price_delivery').html('бесплатно');
    $('#full_price').html(price_order);
  } else {
    $('#validationCustom03').prop('disabled', false);
    var price_order = $('#price_order').html();

    if (price_order <= 500) {
      $('#price_delivery').html('50 руб');
      $('#full_price').html(+price_order + 50);
    } else {
      $('#price_delivery').html('бесплатно');
      $('#full_price').html(price_order);
    }
  }
});
$(function () {
  function saveAllChange() {
    $('.photo-card .td').each(function () {
      var formatData = $(this).find('select[name="format"]').val();
      var countData = parseInt($(this).find('.photocount').val());
      var typeData = $(this).find('input[type="radio"]:checked').val();
      var photoId = $(this).find('.formatselect').children().data('id');
      console.log(formatData, countData, typeData, photoId);
      $.ajax({
        headers: {
          "X-CSRFToken": document.csrf_token
        },
        type: 'POST',
        url: 'confirm/',
        data: {
          'format': formatData,
          'id': photoId
        },
        dataType: 'json',
        success: function success() {}
      });
      $.ajax({
        headers: {
          "X-CSRFToken": document.csrf_token
        },
        type: 'POST',
        url: 'confirm/',
        data: {
          'count': countData,
          'id': photoId
        },
        dataType: 'json',
        success: function success() {}
      });
      $.ajax({
        headers: {
          "X-CSRFToken": document.csrf_token
        },
        type: 'POST',
        url: 'confirm/',
        data: {
          'papier': typeData,
          'id': photoId
        },
        dataType: 'json',
        success: function success() {}
      });
    });
  }

  function changeAllOrder() {
    $('.all-order-change').each(function () {
      var format = $(this).find('select[name=all_format]').val();
      var count = parseInt($(this).find('.all_photocount').val());
      var type = $(this).find('input[name="papier_type"]:checked').val();
      $('.photo-card .td').each(function () {
        $(this).find('select[name="format"]').val(format);
        $(this).find('.photocount').val(count);

        if (type == 'Глянцевая') {
          $(this).find('input[type="radio"][value="Глянцевая"]').prop('checked', true);
        } else {
          $(this).find('input[type="radio"][value="Матовая"]').prop('checked', true);
        }
      });
    });
  }

  $('.change-order').click(function () {
    changeAllOrder();
    calcOrder();
    saveAllChange();
  });
  $('.change-order-show').click(function () {
    $('.all-order-change').modal('show');
  });
  $('.modal-dialog #all-order-change-close').click(function () {
    console.log('kjhjhkjhdsa');
    $('.all-order-change').modal('hide');
  });
});