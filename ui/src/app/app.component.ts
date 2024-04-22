import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {EqualizerComponent} from "./components/equalizer/equalizer.component";
import {FileLoaderComponent} from "./components/file-loader/file-loader.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, EqualizerComponent, FileLoaderComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'ui';
}
