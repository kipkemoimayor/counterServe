import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/service/api.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  posts: any[];
  paginator: any[] = [];
  topPost: void;

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getPosts(1)
  }


  getPosts(pageInd: number): void {
    this.apiService.getPosts(pageInd).subscribe(response => {
      this.posts = response.results;
      this.topPost = this.posts.sort((a, b) => b.view - a.views)[0]
      this.createPaginator(response.count)
    }, error => {
      console.log(error);
    })
  }


  createPaginator(length: number) {
    let paginator = [];
    length = Math.ceil(length / 10);
    for (let i = 0; i < length; i++) {
      paginator.push(i + 1);
    }
    this.paginator = paginator;
  }

  getData(pageInd: number) {
    this.getPosts(pageInd)
  }


}
