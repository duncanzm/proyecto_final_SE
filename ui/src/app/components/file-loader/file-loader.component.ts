import {Component, effect, signal} from '@angular/core';
import {faPlay} from "@fortawesome/free-solid-svg-icons/faPlay";
import {FaIconComponent} from "@fortawesome/angular-fontawesome";
import {faUpload} from "@fortawesome/free-solid-svg-icons";
import {FileDropDirective} from "../../directives/file-drop.directive";
import {NgIf} from "@angular/common";
import {EqualizerComponent} from "../equalizer/equalizer.component";
import {LoadingComponent} from "../shared/loading/loading.component";
import {Frequencies} from "../../../models/frequencies";
import Swal from 'sweetalert2'

@Component({
  selector: 'app-file-loader',
  standalone: true,
  imports: [
    FaIconComponent,
    FileDropDirective,
    NgIf,
    EqualizerComponent,
    LoadingComponent
  ],
  templateUrl: './file-loader.component.html',
  styleUrl: './file-loader.component.css'
})
export class FileLoaderComponent {

  protected readonly faPlay = faPlay;
  protected readonly faUpload = faUpload;

  dataLoaded: Frequencies | null = null;


  constructor(){

  }

  onFilesDropped(files: FileList): void {
    this.handleFiles(files);
  }

  fileInputChange(event: any): void {
    this.handleFiles(event.target.files);
  }

  private handleFiles(files: FileList): void {
    // Handle the file processing here
    Array.from(files).forEach(file => {
      //read content of file
      const reader = new FileReader();
      reader.onload = (e) => {
        let contentString;
        try {
          contentString = atob(reader.result as string);
        }catch (e) {
          Swal.fire({
            title: 'Error!',
            text: 'The file is corrupted',
            icon: 'error',
            confirmButtonText: 'Ok'
          })
          return;
        }

        const frequencies = JSON.parse(contentString);
        this.dataLoaded = frequencies[0];
      };
      reader.readAsText(file);
    });
  }

  resetData() {
    this.dataLoaded = null;
  }
}
