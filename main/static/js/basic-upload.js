$(function() {

    $(".js-upload-photos").click(function() {
        $("#fileupload").click();

    });

    var onDeleteClick = function() {
        var photoId = $(this).data('id'); // $(this).attr('data-id')

        $.post('/' + photoId + '/delete/', {
            'csrfmiddlewaretoken': document.csrf_token,
        });
        $(this).closest('.td').remove();
    };


    function calcOrder() {

        var costs = JSON.parse(service_info)

        var order_info = []; // [{"format": "10x15", count: 1, type: 'glance'}]

        $('.photo-card .td').each(function() {
            var format = $(this).find('select[name="format"]').val();
            var count = parseInt($(this).find('.photocount').val());

            order_info.push({
                "format": format,
                "count": count,
                "type": $(this).find('input[type="radio"]:checked').val(),
            });
        });

        // group by format, type
        var format_type_to_count = {};
        for (let photo of order_info) {
            if (typeof format_type_to_count[`${photo.format}-${photo.type}`] == 'undefined')
                format_type_to_count[`${photo.format}-${photo.type}`] = {
                    'format': photo.format,
                    'type': photo.type,
                    'cost': costs[photo.format],
                    'count': 0
                };
            format_type_to_count[`${photo.format}-${photo.type}`].count += photo.count;
        }

        // render data
        var table = '';
        var price = 0;
        for (const [key, row] of Object.entries(format_type_to_count)) {
            price += row.count * row.cost
            table += "<tr><td>" + row.format +
                "</td><td>" + row.type +
                "</td><td>" + row.count +
                "</td><td>" + row.cost +
                "</td><td>" + row.count * row.cost + "</td></tr>"
        }
        if (table) {
            $('.table-head').html(
                "<tr>" +
                " <th class='container d-flex justify-content-between flex-column flex-lg-row'>" +
                "<div class='col-lg-8 col-12'>" +
                "<p>Ваш заказ:</p>" +
                "<table class='table table-bordered border-primary text-center order-table'>" +
                "<tr><td>Формат</td><td>Бумага</td><td>Кол-во, шт</td><td>Цена, руб</td><td>Стоимость, руб</td></tr>" +
                table +
                "</table>" +
                "</div>" +
                "<div class='col-lg-4 col-12 text-lg-end text-center'>" +
                "<p>Cтоимость заказа: " + price + " руб" + "</p>" +
                "<div class='col-12 d-flex justify-content-between'>" +
                "<button type='button' class='btn btn-primary change-order-show m-lg-3 col-lg-5 col-5'>" +
                "<span class='glyphicon glyphicon-cloud-upload'></span>Пакетное изменение заказа" +
                "</button>" +
                "<a href='/complite/' class='mt-lg-3 col-lg-5 col-5'>" +
                "<button class='btn btn-danger w-100' type='submit'>Оформить заказ</button>" +
                "</a>" +
                "</div>" +
                "</div>" +
                "</th>" +
                "</tr>"
            );
        } else {
            $('.table-head').html('')
        }
        $('.change-order-show').click(function() {
            $('.all-order-change').modal('show');
        });
        $('.modal-dialog #all-order-change-close').click(function() {
            $('.all-order-change').modal('hide');
        });
    }

    $(document).ready(function() {
        calcOrder();
        $('.order-data').click(calcOrder);
        $('.order-data').change(calcOrder);
    });

    var formatSelect = function() {
        var photoId = $(this).children().data('id');

        var formData = $(this).val();
        $.ajax({
            headers: {
                "X-CSRFToken": document.csrf_token
            },
            type: 'POST',
            url: 'confirm/',
            data: {
                'format': formData,
                'id': photoId,
            },
            dataType: 'json',
            success: function() {

            }

        })
    };


    var photoCount = function() {
        var photoId = $(this).data('id');

        var countData = $(this).val();

        $.ajax({
            headers: {
                "X-CSRFToken": document.csrf_token
            },
            type: 'POST',
            url: 'confirm/',
            data: {
                'count': countData,
                'id': photoId,
            },
            dataType: 'json',
            success: function() {

            }

        })
    }

    var photoPapier = function() {
        var photoId = $(this).data('id');

        var papierData = $(this).val();

        $.ajax({
            headers: {
                "X-CSRFToken": document.csrf_token
            },
            type: 'POST',
            url: 'confirm/',
            data: {
                'papier': papierData,
                'id': photoId,
            },
            dataType: 'json',
            success: function() {

            }

        })
    }

    var service_info;
    $("#fileupload").fileupload({

        dataType: 'json',
        sequentialUploads: true,
        /* 1. SEND THE FILES ONE BY ONE */
        start: function(e) { /* 2. WHEN THE UPLOADING PROCESS STARTS, SHOW THE MODAL */
            $("#modal-progress").modal('show');
        },
        stop: function(e) { /* 3. WHEN THE UPLOADING PROCESS FINALIZE, HIDE THE MODAL */
            $("#modal-progress").modal('hide');
            calcOrder();
        },

        progressall: function(e, data) { /* 4. UPDATE THE PROGRESS BAR */
            var progress = parseInt(data.loaded / data.total * 100, 10);
            var strProgress = progress + "%";
            $(".progress-bar").css({ "width": strProgress });
            $(".progress-bar").text(strProgress);

        },

        done: function(e, data) {
            var i = 0;
            var option = "";
            $.each(data.result.format, function() {

                service_info = (data.result.service_data);
                option += "<option data-id='" + data.result.id + "' value='" + data.result.format[i][0] + "'>" + data.result.format[i][0] + "</option>";
                i++;
            })
            if (data.result.is_valid) {
                $(".photo-card").prepend(
                    "<div class='td col-lg-2 col-md-3 col-sm-6'>" +
                    "<a href='" + data.result.url + "'>" +
                    "<div class='order-photo'>" +
                    "<img data-fancybox='order' src='" + data.result.url + "'>" +
                    "</div>" +
                    "</a>" +
                    "<div>" +
                    "<input type='image' src='../static/img/x-button.png' class='delete-photo order-data' data-id='" + data.result.id + "'></input>" +
                    "<p>Формат фотографии</p>" +
                    "<select name='format' class='formatselect form-select order-data'>" +
                    option +
                    "</select>" +
                    "Кол-во <input class='photocount order-data' type='number' value='" + data.result.count + "' data-id='" + data.result.id + "' min='1'> шт" +
                    "<div class='col text-start'>" +
                    "<div class='col-md-12 m-auto'><input class='photopapier order-data' type='radio' name='papier" + data.result.id + "' value='Глянцевая' data-id='" + data.result.id + "' checked><span>Глянцевая</span></div>" +
                    "<div class='col-md-12 m-auto'><input class='photopapier order-data' type='radio' name='papier" + data.result.id + "' value='Матовая' data-id='" + data.result.id + "'><span>Матовая</span></div>" +
                    "</div>" +
                    "</div>"
                )


                $(".delete-photo").unbind('click');
                $(".delete-photo").click(onDeleteClick);
                $('.formatselect').unbind('change');
                $('.formatselect').on('change', formatSelect);
                $('.photocount').unbind('change');
                $('.photocount').on('change', photoCount);
                $('.photopapier').unbind('change');
                $('.photopapier').on('change', photoPapier);
                $('.order-data').click(calcOrder);
                $('.order-data').change(calcOrder);

            }


        }

    });
    $('.formatselect').on('change', formatSelect);
    $('.photocount').on('change', photoCount);
    $('.photopapier').on('change', photoPapier);
    $(".delete-photo").click(onDeleteClick);

    var patname = window.location.pathname

    if (patname == '/order/') {
        calcOrder();
    }


});