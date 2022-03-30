function getDistance(x1, y1, x2, y2) {
    let y = x2 - x1;
    let x = y2 - y1;

    return Math.sqrt(x * x + y * y);
}

var zones = {
    "baikal1": {
        type: "img",
        pano: "https://cdn.glitch.global/e16f5e56-c882-4834-a302-29605aaa4e28/baikal-1-min.jpg?v=1644759629016",
    },
    "baikal2": {
        type: "img",
        pano: "https://cdn.glitch.global/e16f5e56-c882-4834-a302-29605aaa4e28/baikal-2-min.jpg?v=1644759630812",
    },
    "baikal3": {
        type: "img",
        pano: "https://cdn.glitch.global/e16f5e56-c882-4834-a302-29605aaa4e28/baikal-3-min.jpg?v=1644759856208",
    },
    "home": {
        type: "img",
        pano: "https://cdn.glitch.global/e16f5e56-c882-4834-a302-29605aaa4e28/360_F_366041898_gSewr7LZE2Vhf1a51U7IS1FBnUcvxBdU.jpg?v=1648047744117",
    },
};

var domain = "home";
var zone = zones[domain];
var player = null;
var distances = {};

window.onload = (event) => {
    player = document.querySelector("#player");
};

AFRAME.registerComponent('interactive-portal', {
    schema: {
        key: { type: 'string' },
    },

    init: function () {
        let el = this.el;

        setInterval(() => {

            if (player) {
                let p_p = player.getAttribute('position');
                let e_p = el.getAttribute('position');


                distances[this.data.key] = getDistance(p_p.x, p_p.z, e_p.x, e_p.z);

                if (distances[this.data.key] < 0.5) {
                    if (el.getAttribute("visible") == true) {

                        document.querySelectorAll("*[interactive-portal]").forEach((elem) => {
                            elem.setAttribute("visible", true);
                        });
                        el.setAttribute("visible", false);
                        domain = this.data.key;
                        zone = zones[domain];

                        if (zone.type == "img") {
                            document.querySelector("a-sky").setAttribute("src", zone.pano);
                        } else {
                            document.querySelector("a-sky").setAttribute("src", "");
                            document.querySelector("a-sky").setAttribute("color", zone.pano);
                        }

                    }
                }
            }
        }, 300);
    },
});


AFRAME.registerShader("shaderportal", {
    schema: {
        backgroundColor: { default: "white", type: "color", is: "uniform" },
        isGrayscale: { type: "int", is: "uniform", default: 0.0 },
        pano: { type: "map", is: "uniform" },
        time: { type: "time", is: "uniform" },
    },

    vertexShader:
        document.getElementById('vertexShader').textContent,
    fragmentShader:
        document.getElementById('fragmentShader').textContent,
});
