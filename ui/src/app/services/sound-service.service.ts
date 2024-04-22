import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SoundServiceService {

  private audioContext: AudioContext;

  constructor() {
    this.audioContext = new AudioContext();
  }


  generateSineWave(frequency: number): void {
    console.log('Deberia sonar una frecuencia de ' + frequency + 'Hz');
    const audioCtx = new AudioContext();
    const oscNode = new OscillatorNode(audioCtx, {
      type: "sine",
      frequency: frequency,
    });

    const gainNode = new GainNode(audioCtx, {
      // The default value is `1`. We reduce the volume to half of that.
      gain: 0.075,
      // gain: 1
    });


    oscNode.connect(gainNode).connect(audioCtx.destination);

    oscNode.start();
    setTimeout(() => oscNode.stop(), 500);

  }
}
