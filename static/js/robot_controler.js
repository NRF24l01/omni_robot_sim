$(document).ready(function () {
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const robotImage = new Image();
    robotImage.src = '/static/images/omni_main.png';

    const fieldWidthMM = 3000;
    const fieldHeightMM = 2000;
    const robotWidthMM = 270;
    const robotHeightMM = 270;

    function updateRobotPosition(x, y, angle) {
        const canvasWidth = canvas.width;
        const canvasHeight = canvas.height;
        const posX = (x / fieldWidthMM) * canvasWidth;
        const posY = (y / fieldHeightMM) * canvasHeight;
        const robotWidth = (robotWidthMM / fieldWidthMM) * canvasWidth;
        const robotHeight = (robotHeightMM / fieldHeightMM) * canvasHeight;

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.save();
        ctx.translate(posX, posY);
        ctx.rotate(angle * Math.PI / 180);
        ctx.drawImage(robotImage, -robotWidth / 2, -robotHeight / 2, robotWidth, robotHeight);
        ctx.restore();
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