'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');
var watch = require('gulp-watch');
var minifycss = require('gulp-minify-css');
var rename = require('gulp-rename');
var gzip = require('gulp-gzip');
var livereload = require('gulp-livereload');
var cleanCSS = require('gulp-clean-css');

var gzip_options = {
    threshold: '1kb',
    gzipOptions: {
        level: 9
    }
};

/* Compile Our Sass */
gulp.task('sass', function() {
    return gulp.src('static/scss/*.scss')
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest('static/stylesheets'))
        .pipe(rename({suffix: '.min'}))
        .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(minifycss())
        .pipe(gulp.dest('static/stylesheets'))
        .pipe(gzip(gzip_options))
        .pipe(gulp.dest('static/stylesheets'))
        .pipe(livereload());
});

/* Watch Files For Changes */
gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('static/scss/**/*.scss', ['sass']);

    /* Trigger a live reload on any Django template changes */
    gulp.watch('**/templates/*').on('change', livereload.changed);
});

gulp.task('default', ['sass', 'watch']);
