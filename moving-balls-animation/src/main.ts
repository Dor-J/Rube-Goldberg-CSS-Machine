import './style.css'

const app = document.querySelector<HTMLDivElement>('#app')

if (!app) {
  throw new Error('Root #app element not found')
}

app.innerHTML = `
  <div class="stage" aria-label="Static render of a Rube-Goldberg inspired machine">
    <div
      class="machine"
      role="img"
      aria-label="Blue capsule tube, spiral coil, ramp, funnel, ring assembly, wavy slide and four cue balls"
    >
      <div class="shape tube" aria-hidden="true"></div>

      <div class="shape coil" aria-hidden="true">
        <svg viewBox="0 0 150 240" role="presentation" aria-hidden="true">
          <path
            class="coil-back"
            d="M75 18 C 135 18 135 78 75 78 S 15 138 75 138 S 125 198 75 198 S 45 230 75 230"
          ></path>
          <path
            class="coil-front"
            d="M75 18 C 135 18 135 78 75 78 S 20 138 75 138 S 120 188 75 188 S 50 228 75 228"
          ></path>
        </svg>
        <div class="coil-cap" aria-hidden="true"></div>
        <div class="coil-tail" aria-hidden="true"></div>
      </div>

      <div class="shape ramp" aria-hidden="true"></div>
      <div class="shape ramp-block" aria-hidden="true"></div>

      <div class="shape funnel" aria-hidden="true">
        <div class="mouth" aria-hidden="true"></div>
        <div class="body" aria-hidden="true"></div>
        <span class="confetti c1" aria-hidden="true"></span>
        <span class="confetti c2" aria-hidden="true"></span>
        <span class="confetti c3" aria-hidden="true"></span>
        <span class="confetti c4" aria-hidden="true"></span>
      </div>

      <div class="shape ring-assembly" aria-hidden="true">
        <div class="circle" aria-hidden="true"></div>
        <div class="pole" aria-hidden="true"></div>
        <div class="piston p1" aria-hidden="true"></div>
        <div class="piston p2" aria-hidden="true"></div>
        <div class="piston p3" aria-hidden="true"></div>
      </div>

      <div class="shape slide" aria-hidden="true">
        <div class="berm" aria-hidden="true"></div>
        <div class="hole" aria-hidden="true"></div>
        <svg viewBox="0 0 300 90" class="wave" role="presentation" aria-hidden="true">
          <path d="M10 60 Q60 15 110 60 T210 60 T290 60"></path>
        </svg>
      </div>

      <div class="ball b-coil" aria-hidden="true"></div>
      <div class="ball b-tube" aria-hidden="true"></div>
      <div class="ball b-ring" aria-hidden="true"></div>
      <div class="ball b-exit" aria-hidden="true"></div>
    </div>
  </div>
`
