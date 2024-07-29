$(document).ready(function () {
    const field = $('#field');
    const robot = $('#robot');

    function updateRobotPosition(x, y, angle) {
        const fieldWidth = field.width();
        const fieldHeight = field.height();
        const posX = (x / 3000) * fieldWidth;
        const posY = (y / 2000) * fieldHeight;
        robot.css('left', posX + 'px');
        robot.css('top', posY + 'px');
        robot.css('transform', 'rotate(' + angle + 'deg)');
    }

    function getPosition() {
        $.get('/get_position', function (data) {
            updateRobotPosition(data.x, data.y, data.angle);
        });
    }

    $('#control-form').submit(function (event) {
        event.preventDefault();
        const speed1 = $('#speed1').val();
        const speed2 = $('#speed2').val();
        const speed3 = $('#speed3').val();
        const time = $('#time').val();

        $.ajax({
            url: '/set_movement',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({speed1: speed1, speed2: speed2, speed3: speed3, time: time}),
            success: function (data) {
                updateRobotPosition(data.x, data.y, data.angle);
            }
        });
    });

    getPosition();
});
