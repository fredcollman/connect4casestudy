module.exports = function(grunt) {
	grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
	  sass: {
	    dist: {
	      files: [{
	        expand: true,
	        cwd: 'styles',
	        src: ['main.scss'],
	        dest: 'static/css',
	        ext: '.css',
	      }]
	    }
	  },
	  watch: {
  		css: {
		    files: 'styles/**/*.scss',
		    tasks: ['sass'],
		    options: {
		      livereload: true,
		    },
		  },
		  livereload: {
		  	files: '**/*.html',
		  	options: {
		  		livereload: true,
		  	}
		  },
		  jasmine: {
		  	files: 'js/**/*.js',
		  	tasks: ['jasmine', 'copy:main'],
		  	options: {
		  		livereload: true,
		  	}
		  },
		},
	  jasmine: {
	    main: {
	      src: 'js/src/**/*.js',
	      options: {
	        specs: 'js/spec/**/*_spec.js',
	        helpers: 'js/spec/**/*_helper.js',
	      }
	    }
	  },
	  copy: {
	  	main: {
	  		files: [
	  			{
	  				expand: true, 
	  				cwd: 'js/src',
	  				src: ['**'], 
	  				dest: 'static/js',
	  			},
  			]
  		},
  		bower: {
  			files: [
	  			{
	  				src: ['bower_components/jquery/dist/jquery.min.js'],
	  				dest: 'static/js/jquery.min.js',
	  			},
	  			{
	  				src: ['bower_components/Materialize/dist/js/materialize.min.js'],
	  				dest: 'static/js/materialize.min.js',
	  			},
	  			{
	  				expand: true,
	  				cwd: 'bower_components/Materialize/fonts',
	  				src: ['**'],
	  				dest: 'static/fonts',
	  			},
	  		]
	  	}
	  },
	});

	grunt.loadNpmTasks('grunt-contrib-sass');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-jasmine');
	grunt.loadNpmTasks('grunt-contrib-copy');

	grunt.registerTask('dev', ['watch']);
	grunt.registerTask('dist', ['sass', 'copy']);
};
