jQuery(function($){
    var $myForms = $(".forms-perso");
    $myForms.css("display", "none");
	
	// change the displayed form in function of the checkbox checked.
	$('input:radio').change(
    function(){
        if ($(this).is(':checked')) {
			$myForms.css("display", "none");
			$('#'+$(this).attr('value')).css("display", "block");
        } 
		else {
			$myForms.css("display", "none");
		}
    });
	
	$('.select-perso').focus(
	function() {
		//alert('a select has the focus');
	});
	
	$('.select-perso').change(
	function() {
		//alert('the value of the select has been set to : ' + $(this).find("option:selected").text());
		
		$.ajax({
		   url : 'more_com.php',
		   type : 'GET',
		   dataType : 'html',
		   success : function(code_html, statut){        
		   },
		   error : function(resultat, statut, erreur){
		   },
		   complete : function(resultat, statut){
		   }
		});
		
		$.get(
			'fichier_cible.php', // Le fichier cible côté serveur.
			'false', // Nous utilisons false, pour dire que nous n'envoyons pas de données.
			'nom_fonction_retour', // Nous renseignons uniquement le nom de la fonction de retour.
			'text' // Format des données reçues.
		);

		function nom_fonction_retour(texte_recu){
		}
		
	});		
});