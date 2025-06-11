
def generate_classifier_block(sample_num, transcript):
    sample_id = f"sample_{sample_num:03d}"
    audio_url = f"https://rlataewoo.github.io/eval_sample/samples/table_1/gigaspeech_mp3/{sample_id}.mp3?raw=true"
    
    return f"""
    <crowd-classifier 
        categories="['Excellent - Completely natural speech - 5', '4.5', 'Good - Mostly natural speech - 4', '3.5', 'Fair - Equally natural and unnatural speech - 3', '2.5', 'Poor - Mostly unnatural speech - 2', '1.5', 'Bad - Completely unnatural speech - 1']"
        header="How natural does the edited segment of the speech sound? Please focus on whether the transition between the original and synthesized parts is smooth and human-like."
        name="{sample_id}-naturalness">
            <classification-target>
                <audio controls style="width: 100%">
                    <source src="{audio_url}" type="audio/mp3" />
                </audio>
                <div class="sample-number" style="margin-top: 10px; margin-bottom: 10px; font-weight: bold; font-size: 30px;">Sample {sample_num:03d}</div>
                <div id="text_area">
                    <h3>Transcripts (edited parts are shown in <span style='color: red;'>red</span>)</h3>
                    <p>{transcript}</p>
                </div>
            </classification-target>
        <short-instructions>  
            <p>
              Listen to the sample of computer generated speech and assess the quality 
              of the audio based on how close it is to natural speech. The words in the audio are shown in the Original utterance below.
            </p>
            For better results, wear headphones and work in a quiet environment.
            If the audio file is not playing, please be patient as it may take some time for the audio file to upload.
        </short-instructions>
    </crowd-classifier>
    """

def generate_hit_file(filename, start_idx, end_idx, transcript_map):
    html_blocks = ['<!-- You must include this JavaScript file -->',
                   '<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>',
                   '<crowd-form answer-format="flatten-objects">']
    
    for i in range(start_idx, end_idx + 1):
        transcript = next(val for key, val in transcript_map.items() if i in key)
        html_blocks.append(generate_classifier_block(i, transcript))

    html_blocks.append('</crowd-form>')

    full_html = '\n'.join(html_blocks)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_html)

# 각 샘플 번호와 대응하는 텍스트
transcript_map = {
    range(1, 7+1): "WE THOUGHT SIGNIFICANTLY <span style='color: red;'>ABOUT BUYING THE IRVINE CORPORATION</span> WHEN IT BECAME AVAILABLE SO.",
    range(8, 14+1): "FEW ACTORS HAVE <span style='color: red;'>MANAGED TO SIMULTANEOUSLY CULTIVATE A REPUTATION</span> AS A SERIOUS DRAMATIC ACTOR.",
    range(15, 21+1): "WE KNOW THAT YODA LIVED TO THE RIPE OLD AGE OF NINE <span style='color: red;'>HUNDRED IN RETURN OF THE JEDI WHICH EVERYONE ELSE IS SURPRISED ABOUT BUT HE ISN'T</span> SEEMING TO INDICATE THAT IT'S NOT REALLY THAT BIG OF A DEAL FOR HIM.",
    range(22, 28+1): "PRETTY MUCH ALL WE <span style='color: red;'>CAN TELL YOU IS THAT THIS INSTALLMENT</span> FOLLOWS THE EVENTS OF EPISODE SEVEN.",
    range(29, 35+1): "YOU ARE GONNA HAVE AMBIENT IF YOU ARE ON <span style='color: red;'>THE BIKE YOU'RE CYCLING YOU COULD HEAR IF IF A CAR</span> HONKS ITS HORN OR SOMETHING. THIS COULD REALLY AMPLIFY YOUR SURROUNDINGS.",
    range(36, 42+1): "HE MAY BE ON <span style='color: red;'>AIR ON SATURDAY SHE WAS GONNA</span> CO CO-STAR THE U F C.",
    range(43, 49+1): "PRESENTING THE APOCALYPTIC ADVENTURE <span style='color: red;'>OF AN ELEVEN YEAR OLD BOY NAMED</span> JAKE CHAMBERS AS HE ACCIDENTALLY UNCOVERS.",
    range(50, 56+1): "YEAH WHATEVER IS RIGHTS OF ANOTHER FIVE DOLLARS <span style='color: red;'>DO YOU THINK PAPA G IT IS WERE PROBABLY THREE</span> OR FOUR BUCKS AWAY FROM FROM GETTING HIM TO GO.",
    range(57, 63+1): "EVEN THOUGH AS A TEAM WE <span style='color: red;'>HAD YOU KNOW WE WE WE WERE IN LAST</span> PLACE FOR ME IT WASN'T A BAD CUT.",
    range(64, 70+1): "IT ALSO ENSURES FOR THE FIRST TIME <span style='color: red;'>THAT THE LAWS CANNOT TREAT PEOPLE DIFFERENTLY BASED ON</span> THEIR RACE. THIS IS CALLED THE EQUAL PROTECTION CLAUSE.",

    range(71, 77+1): "BUT THEN I'M ALWAYS AT HOME. <span style='color: red;'>ONE BOGGY PLACE IS MUCH LIKE ANOTHER AND</span> I DON'T HOLD WITH ALL THIS PACKING UP.",
    range(78, 84+1): "A BONUS CHECK THIRD <span style='color: red;'>IN TEN FLIES OVER HIS HEAD AND</span> FALL ON ON IT BUT THIRTY-FOUR.",
    range(85, 91+1): "FROM THEIR LESSER KNOWN ORIGINS IN THAILAND TO THEIR <span style='color: red;'>RISE AS A GLOBAL MARKETING EMPIRE. IF YOU'D LIKE TO WATCH</span> THE FULL BEHIND THE BUSINESS SERIES YOU CAN CLICK HERE.",
    range(92, 98+1): "WE JUST HIT NEXT WE GO THROUGH WE CREATE AN <span style='color: red;'>AD I UNDERSTAND I AM PAYING FOR MY OWN AD SPEND THEN WE</span> COME OVER HERE TARGET CITY WE'LL SAY WE ARE GOING FOR PHOENIX.",
    range(99, 105+1): "I WOULD ALSO TAKE WHATEVER IS <span style='color: red;'>LEFT BECAUSE SOMETHING IS BETTER THAN NOTHING FOR PEOPLE</span> WHO ARE STRUGGLING EVEN THOUGH IT'S NOT MUCH.",
    range(106, 112+1): "LIKE I REALLY <span style='color: red;'>DON'T GET ANNOYED WITH MIKE CAUSE</span> HE HAS CHARACTER AND INTEGRITY.",
    range(113, 119+1): "YOU MAY THINK THAT YOU HAVE A RATIONAL <span style='color: red;'>JUSTIFICATION FOR EVERY VIEW THAT YOU HOLD. YOU MAY THINK</span> IT'S THE GREATEST WORLDVIEW THAT IT'S EVER BEEN CREATED.",
    range(120, 126+1): "YOU ARE A RESIDENT OF NEW YORK STATE <span style='color: red;'>THERE IS A SEAT THAT IS OPEN AND YOU HAVE</span> THE ABILITY TO TAKE THAT SEAT IN MANY PEOPLE'S OPINION.",
    range(127, 133+1): "SO LET'S TAKE THAT LINK AND <span style='color: red;'>JUMP INTO OUR FACEBOOK. HERE I AM INSIDE</span> OF MY FACEBOOK PAGE FOR COREY ASH.",
    range(134, 140+1): "I DID GIVE UP <span style='color: red;'>BUT I SHOULDN'T HAVE. I I MUST</span> KEEP TRYING AND YOU SHOULD TOO.",

    range(141, 147+1): "WHERE DO WE WANNA SEND THEM? SO OVER HERE GUYS <span style='color: red;'>WE HAVE YOUR FACEBOOK PAGE YOU CAN HAVE THEM GO TO YOUR</span> WEBSITE YOU CAN HAVE THEM BOOK AN APPOINTMENT WITH YOU OR.",
    range(148, 154+1): "THE EUROPEAN IN AFRICA IS <span style='color: red;'>AN EXPAT AND THE AFRICAN IN EUROPEAN IS</span> A MIGRANT. IT CAN'T CONTINUE LIKE THAT.",
    range(155, 161+1): "AND STUDIES HAVE SHOWN THAT WHEN WE GIVE <span style='color: red;'>IT TRIGGERS THE SAME CHEMICAL REACTIONS IN OUR BRAINS IS FALLING</span> IN LOVE OR BONDING WITH A NEWBORN CHILD.",
    range(162, 168+1): "A DISEASE IS <span style='color: red;'>NOT GONNA IF YOU LOOK</span> AT THE NUMBERS AT YOUTA.",
    range(169, 175+1): "REMEMBER HOW EARLIER I SAID THESE NEURONS ARE <span style='color: red;'>SIMPLY THINGS THAT HOLD NUMBERS WELL OF COURSE THE SPECIFIC NUMBERS</span> THAT THEY HOLD DEPENDS ON THE IMAGE YOU FEED IN.",
    range(176, 182+1): "WHAT'S INTERESTING IS THAT YOU WROTE IT <span style='color: red;'>TOGETHER. YOU'VE WRITTEN MANY BOOKS SEPARATELY BUT THIS WAS</span> YOUR FIRST BOOK WRITING TOGETHER AS MOTHER AND DAUGHTER.",
    range(183, 189+1): "AND YEAH WE WE ENDED UP <span style='color: red;'>IN THE SAME SPOT SO THERE'D BE LESSON</span> KIDS IS TO AH NOT BE RESPONSIBLE.",
    range(190, 196+1): "THIS IS JUST SO <span style='color: red;'>COZY UP HERE. AND HAVING THAT</span> SKYLIGHT IS JUST LOVELY ISN'T IT.",
    range(197, 203+1): "YES YES OKAY SO I'LL PUT A LINK <span style='color: red;'>TO ALL THAT STUFF IN THE SHOW NOTES FOR YOU</span> GUYS AS WELL AS KATIE'S AWESOME OF THE WEEK.",
    range(204, 210+1): "WHEN YOU'RE MAKING DECISIONS THAT'S A GOOD THAT'S A TRAIT OF <span style='color: red;'>A GOOD HUMAN BEING TO DO THAT BY THE WAY IT DOESN'T DOESN'T</span> MAKE YOU WEAK TO CONSIDER THE FEELINGS AND PLIGHT OF OTHER PEOPLE.",

    range(211, 217+1): "WITH TWO COLLEAGUES <span style='color: red;'>I WORKED UM SORT OF BUILDING</span> A DISTRIBUTION AND WE WE.",
    range(218, 224+1): "AND THERE ISN'T JUST <span style='color: red;'>ONE DELIVERY THAT HAPPENS AT THE</span> BEGINNING OF A SEASON. NO NO.",
    range(225, 231+1): "WELL THE DIFFICULTIES THEY HAVE IS COMMUNICATING WITH YOUNG PEOPLE BECAUSE <span style='color: red;'>CONSERVATIVES WHAT WHAT THE HELL ARE THEY GONNA SELL TO YOUNG PEOPLE RIGHT CAUSE</span> BEING CONSERVATIVE IS SOMETHING THAT HAPPENS WHEN YOU'RE OLDER.",
    range(232, 238+1): "AT THE END OF THIS COURSE <span style='color: red;'>YOU WILL BE ABLE TO EXPLAIN THE THREE FUNDAMENTAL</span> CHARACTERISTIC THAT DEFINE THE BLOCKCHAIN USING BITCOIN BLOCKCHAIN.",
    range(239, 245+1): "YOU GET THE TRASH OUT IF <span style='color: red;'>I GET STEVE COME OVER HERE PUT HIS</span> DAMN HANDS ON YOU AGAIN OH OH.",
    range(246, 252+1): "AND IT'S AVAILABLE FOR BOTH MAC AND WINDOWS <span style='color: red;'>DOES CAUSE NINETEEN DOLLARS NINETY-NINE FOR THE YEAR FOR A</span> SUBSCRIPTION TO THIS SOFTWARE BUT IT IS SO MUCH MORE.",
    range(253, 259+1): "CLAUDE MONET'S WATER LILIES SERIES <span style='color: red;'>WAS PAINTED AT HIS HOME IN GIVERNY</span> BETWEEN EIGHTEEN NINETY-SIX AND NINETEEN TWENTY-SIX.",
    range(260, 266+1): "I DIDN'T REALIZE THAT <span style='color: red;'>WAS MATH. OH IF THAT'S MATH</span> THEN I COULD DO THAT.",
    range(267, 273+1): "BECAUSE <span style='color: red;'>FAST FASHION HAS AS</span> ITS FUNDAMENTAL PURPOSE.",
    range(274, 280+1): "ROEMER SUPPORTERS WERE NOW <span style='color: red;'>UP FOR GRABS IF THEY VOTED</span> REPUBLICAN IN THE NOVEMBER RUNOFF.",
}

generate_hit_file("hit_1.html", 1, 70, transcript_map)
generate_hit_file("hit_2.html", 71, 140, transcript_map)
generate_hit_file("hit_3.html", 141, 210, transcript_map)
generate_hit_file("hit_4.html", 211, 280, transcript_map)
